import qrcode

REDIRECT_URL = "https://qr.dl.surf/"

img = qrcode.make(REDIRECT_URL)
img.save("app_qr.png")
print("Saved app_qr.png →", REDIRECT_URL)
