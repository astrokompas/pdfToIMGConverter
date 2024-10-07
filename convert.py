import fitz
import os

def pdf_to_images(pdf_path, output_folder, image_format='png', dpi=150):
    pdf_document = fitz.open(pdf_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap(dpi=dpi)
        pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]
        image_filename = f"{output_folder}/{pdf_filename}_page_{page_num + 1}.{image_format}"
        pix.save(image_filename)
        print(f"Saved {image_filename}")

def convert_all_pdfs_in_folder(input_folder, output_folder, image_format='png', dpi=150):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            print(f"Processing {pdf_path}")
            pdf_to_images(pdf_path, output_folder, image_format, dpi)

if __name__ == "__main__":
    input_folder = "."
    output_folder = "."
	
    convert_all_pdfs_in_folder(input_folder, output_folder)
