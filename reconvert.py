import fitz

def images_to_pdf(image_files, output_pdf):
    pdf_document = fitz.open()

    for image_file in image_files:
        img = fitz.open(image_file)
        rect = img[0].rect
        pdfbytes = img.convert_to_pdf()
        img_pdf = fitz.open("pdf", pdfbytes)
        page = pdf_document.new_page(width=rect.width, height=rect.height)
        page.show_pdf_page(rect, img_pdf, 0)

    pdf_document.save(output_pdf)
    pdf_document.close()

if __name__ == "__main__":
    image_files = ["page_1.png", "page_2.png"]
    output_pdf = "reconvert.pdf"
    images_to_pdf(image_files, output_pdf)
    print(f"PDF saved as {output_pdf}")
