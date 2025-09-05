from flask import Flask, request, redirect
import qrcode

app = Flask(__name__)

# URLs
ANDROID_URL = "https://play.google.com/store/apps/details?id=com.dlplatforms.dlsurfmobile"
IOS_URL = "https://apps.apple.com/us/app/gumroad/id916819108"
WEB_URL = "https://dl.surf/social"
FALLBACK_URL = "https://youtube.com/yourvideo"

@app.route("/openapp")
def open_app():
    user_agent = request.headers.get("User-Agent", "").lower()

    if "android" in user_agent:
        return redirect(ANDROID_URL)
    elif "iphone" in user_agent or "ipad" in user_agent or "ios" in user_agent:
        return redirect(IOS_URL)
    elif "windows" in user_agent or "mac" in user_agent or "linux" in user_agent:
        return redirect(WEB_URL)
    else:
        return redirect(FALLBACK_URL)

# Function to generate QR code for the redirect URL
def generate_qr():
    url = "https://yourdomain.com/openapp"  # your hosted Flask endpoint
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save("app_qr.png")
    print("QR code saved as app_qr.png")

if __name__ == "__main__":
    generate_qr()
    app.run(host="0.0.0.0", port=5000)
