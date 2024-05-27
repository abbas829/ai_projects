import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

def generate_qr_code(data):
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
    return img

# Streamlit app
st.title("QR Code Generator")

# Text input for QR code
qr_data = st.text_input("Enter text or URL to generate QR code:")

# Generate QR code button
if st.button("Generate QR Code"):
    if qr_data:
        img = generate_qr_code(qr_data)
        
        # Convert the PIL image to a byte stream
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = buffered.getvalue()
        
        # Display the image in Streamlit
        st.image(img_str, caption='Generated QR Code', use_column_width=True)

        # Provide download link
        st.download_button(
            label="Download QR Code",
            data=img_str,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter text or URL to generate a QR code.")

# Footer
st.markdown("Created by [Your Name](https://yourwebsite.com)")
