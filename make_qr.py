import qrcode

REDIRECT_URL = "https://dlsurf-qr.onrender.com/openapp"

img = qrcode.make(REDIRECT_URL)
img.save("app_qr.png")
print("Saved app_qr.png →", REDIRECT_URL)
