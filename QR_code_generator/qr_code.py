import qrcode

def generate_qr_code(data, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the data to the QR code  
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to a file
    img.save(filename)
    print(f"QR code saved as '{filename}'")

if __name__ == "__main__":
    print("QR Code Generator")
    data = input("Enter the text or URL to encode: ")
    filename = input("Enter the filename (e.g., qrcode.png): ")

    # Generate the QR code
    generate_qr_code(data, filename)
