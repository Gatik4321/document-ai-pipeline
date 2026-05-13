from pathlib import Path
import json
from PyPDF2 import PdfReader

BASE_DIR = Path(__file__).resolve().parent.parent
EXTRACTED_FOLDER = BASE_DIR / "data" / "extracted"
EXTRACTED_FOLDER.mkdir(parents=True, exist_ok=True)


def load_pdf_pages(pdf_path):
    """Load PDF pages into structured Open Data Loader format."""
    reader = PdfReader(pdf_path)
    page_documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = text.strip()

        if not text:
            continue

        page_documents.append({
            "source": Path(pdf_path).name,
            "page": page_number,
            "text": text,
        })

    return page_documents


def save_extracted_pages(pdf_path, page_documents):
    """Save structured page extraction as JSON and markdown."""
    output_path = EXTRACTED_FOLDER / f"{Path(pdf_path).stem}_pages.json"
    payload = {
        "source": Path(pdf_path).name,
        "pages": page_documents,
    }
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    markdown_path = EXTRACTED_FOLDER / f"{Path(pdf_path).stem}_pages.md"
    markdown_lines = []
    for page in page_documents:
        markdown_lines.append(f"## {page['source']} - Page {page['page']}\n\n{page['text']}")

    markdown_path.write_text("\n\n".join(markdown_lines), encoding="utf-8")

    return {
        "json": str(output_path),
        "markdown": str(markdown_path),
    }
