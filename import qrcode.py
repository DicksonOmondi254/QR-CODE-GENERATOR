import qrcode

# Message or URL you want to encode
data = "https://example.com"  # Replace with your own URL or message

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")
