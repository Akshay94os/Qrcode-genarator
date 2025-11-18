import qrcode

# Data to encode
data = "https://www.example.com"

# Creating an instance of QRCode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("qr_code.png")

print("QR Code generated successfully!")
