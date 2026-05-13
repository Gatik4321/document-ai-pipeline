from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF pages using an open-source PDF loader."""
    reader = PdfReader(pdf_path)
    pages = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = text.strip()

        if text:
            pages.append({
                "page": page_num,
                "text": text,
            })

    return pages