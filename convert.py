import fitz
import os

def pdf_to_images(pdf_path, output_folder, image_format='png', dpi=150):
    pdf_document = fitz.open(pdf_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap(dpi=dpi)
        image_filename = f"{output_folder}/page_{page_num + 1}.{image_format}"
        pix.save(image_filename)
        print(f"Saved {image_filename}")

if __name__ == "__main__":
    pdf_path = "CV.pdf"
    output_folder = "."
    pdf_to_images(pdf_path, output_folder)
