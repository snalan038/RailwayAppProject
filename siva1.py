import qrcode

# Text or data you want to encode in the QR code
data = "Hello, World!"

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=4)

# Add data to the QR code
qr.add_data(data)

# Compile the QR code
qr.make(fit=True)

# Generate an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image file
qr_image.save("qrcode.png")
