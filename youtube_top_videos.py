"""Lấy top video nhiều view nhất của các kênh YouTube qua YouTube Data API v3 (chính thức).

Chạy:  export YOUTUBE_API_KEY="..."   # key tạo trên Google Cloud, bật "YouTube Data API v3"
       python youtube_top_videos.py @DrInsanityCrime @DOCS187s
Kết quả: in bảng ra màn hình và ghi file youtube_top_videos.md
"""

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://www.googleapis.com/youtube/v3/"
KEY = os.environ.get("YOUTUBE_API_KEY", "placeholder")  # trong phiên cloud, proxy tự chèn key thật
TOP_N = 18
MAX_PAGES = 20  # tối đa 1000 video mới nhất mỗi kênh, để tiết kiệm quota

DEFAULT_HANDLES = [
    "@File-187-Crime",
    "@DrInsanityCrime",
    "@DOCS187s",
    "@JCS",
    "@LawCrimeInterrogations",
]


def call(endpoint, **params):
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-Goog-Api-Key": KEY})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Lỗi API {e.code} ở {endpoint}: {e.read().decode()[:300]}")


def duration(iso):
    h, m, s = (int(x or 0) for x in re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso).groups())
    return f"{h}:{m:02}:{s:02}" if h else f"{m}:{s:02}"


def channel_report(handle):
    data = call("channels", part="snippet,statistics,contentDetails", forHandle=handle)
    if not data.get("items"):
        return f"## {handle}\n\nKhông tìm thấy kênh với handle này.\n"
    ch = data["items"][0]
    st = ch["statistics"]
    uploads = ch["contentDetails"]["relatedPlaylists"]["uploads"]

    ids, token = [], None
    for _ in range(MAX_PAGES):
        params = {"part": "contentDetails", "playlistId": uploads, "maxResults": 50}
        if token:
            params["pageToken"] = token
        page = call("playlistItems", **params)
        ids += [it["contentDetails"]["videoId"] for it in page.get("items", [])]
        token = page.get("nextPageToken")
        if not token:
            break

    videos = []
    for i in range(0, len(ids), 50):
        batch = call("videos", part="snippet,statistics,contentDetails", id=",".join(ids[i:i + 50]))
        videos += batch.get("items", [])
    videos.sort(key=lambda v: int(v["statistics"].get("viewCount", 0)), reverse=True)

    lines = [
        f"## {ch['snippet']['title']} ({handle})",
        "",
        f"Subscribers: {int(st.get('subscriberCount', 0)):,} · Tổng view: {int(st.get('viewCount', 0)):,} · "
        f"Số video: {st.get('videoCount')} · Đã quét: {len(ids)} video",
        "",
        "| # | Tiêu đề | View | Thời lượng | Ngày đăng | Thumbnail |",
        "|---|---|---|---|---|---|",
    ]
    for n, v in enumerate(videos[:TOP_N], 1):
        sn = v["snippet"]
        thumbs = sn["thumbnails"]
        thumb = (thumbs.get("maxres") or thumbs.get("high") or thumbs.get("default"))["url"]
        title = sn["title"].replace("|", "/")
        lines.append(
            f"| {n} | {title} | {int(v['statistics'].get('viewCount', 0)):,} | "
            f"{duration(v['contentDetails']['duration'])} | {sn['publishedAt'][:10]} | [ảnh]({thumb}) |"
        )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    handles = sys.argv[1:] or DEFAULT_HANDLES
    report = "# Top video theo lượt xem\n\n" + "\n".join(channel_report(h) for h in handles)
    print(report)
    with open("youtube_top_videos.md", "w", encoding="utf-8") as f:
        f.write(report)
