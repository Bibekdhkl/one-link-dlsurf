import os
from flask import Flask, request, redirect

app = Flask(__name__)

ANDROID_URL="https://play.google.com/store/apps/details?id=your.app.id"
IOS_URL="https://apps.apple.com/app/id1234567890"
WEB_URL="https://dl.surf/"
FALLBACK_URL="https://www.youtube.com/@dlsurfofficial"

# ANDROID_URL  = os.getenv("ANDROID_URL")
# IOS_URL      = os.getenv("IOS_URL")
# WEB_URL      = os.getenv("WEB_URL")
# FALLBACK_URL = os.getenv("FALLBACK_URL")

def detect_platform(ua: str) -> str:
    ua = (ua or "").lower()
    if "android" in ua:
        return "android"
    if "iphone" in ua or "ipad" in ua or "ipod" in ua or "ios" in ua:
        return "ios"
    if "windows" in ua or "macintosh" in ua or "x11" in ua or "cros" in ua or ("linux" in ua and "android" not in ua):
        return "web"
    return "other"

@app.get("/")
def openapp():
    override = request.args.get("platform")
    if override in {"android", "ios", "web"}:
        platform = override
    else:
        platform = detect_platform(request.headers.get("User-Agent", ""))

    if platform == "android":
        target = ANDROID_URL
    elif platform == "ios":
        target = IOS_URL
    elif platform == "web":
        target = WEB_URL
    else:
        target = FALLBACK_URL

    return redirect(target, code=302)

@app.get("/health")
def health():
    return {"ok": True}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 2000))
    app.run(host="0.0.0.0", port=port)
