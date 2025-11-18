import qrcode

data = "Python QR Code Example"

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="yellow")
img.save("color_qr.png")
