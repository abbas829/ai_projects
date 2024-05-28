import streamlit as st
import fitz  # PyMuPDF
import io

st.title("PDF Editor")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Load the PDF
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    st.sidebar.write(f"PDF loaded with {pdf_document.page_count} pages.")

    # Select a page to edit
    page_number = st.sidebar.selectbox("Select a page to edit", range(pdf_document.page_count))
    page = pdf_document.load_page(page_number)

    # Render the page
    image = page.get_pixmap()
    image_bytes = image.tobytes("png")
    st.image(image_bytes, caption=f"Page {page_number + 1}", use_column_width=True)

    # Annotation options
    st.sidebar.header("Add Annotation")
    annotation_text = st.sidebar.text_input("Text")
    
    # Ensure numerical consistency by converting width and height to int
    page_width = int(page.rect.width)
    page_height = int(page.rect.height)
    
    annotation_x = st.sidebar.number_input("X coordinate", min_value=0, max_value=page_width, value=50)
    annotation_y = st.sidebar.number_input("Y coordinate", min_value=0, max_value=page_height, value=50)
    annotation_font_size = st.sidebar.number_input("Font size", min_value=1, max_value=50, value=12)
    annotation_color = st.sidebar.color_picker("Color", "#000000")

    if st.sidebar.button("Add Text Annotation"):
        # Add text annotation to the selected page
        page.insert_text((annotation_x, annotation_y), annotation_text, fontsize=annotation_font_size, color=annotation_color)
        st.success(f"Added text annotation to page {page_number + 1}")

        # Re-render the page with the annotation
        image = page.get_pixmap()
        image_bytes = image.tobytes("png")
        st.image(image_bytes, caption=f"Page {page_number + 1} with annotation", use_column_width=True)

    # Save edited PDF
    if st.sidebar.button("Save PDF"):
        output_pdf = io.BytesIO()
        pdf_document.save(output_pdf)
        pdf_document.close()
        st.download_button("Download Edited PDF", data=output_pdf.getvalue(), file_name="edited_document.pdf", mime="application/pdf")
