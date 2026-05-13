from pathlib import Path
import json

class PageIndexStore:
    """Page-level index for document source, page, and metadata."""

    def __init__(self, storage_dir=None):
        base_dir = Path(storage_dir) if storage_dir else Path(__file__).resolve().parent.parent / "data" / "metadata"
        self.storage_dir = base_dir
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.index_path = self.storage_dir / "page_index.json"
        self.documents = []

    def add_documents(self, page_documents):
        """Add page document entries to the page index."""
        self.documents.extend(page_documents)

    def get_by_source(self, source_name):
        """Return all pages for a given source file."""
        return [doc for doc in self.documents if doc["source"] == source_name]

    def get_by_source_page(self, source_name, page_number):
        """Return a single page entry by source and page number."""
        for doc in self.documents:
            if doc["source"] == source_name and doc["page"] == page_number:
                return doc
        return None

    def save(self):
        """Persist the page index to disk."""
        payload = {
            "total_pages": len(self.documents),
            "documents": self.documents,
        }
        self.index_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return str(self.index_path)

    def load(self):
        """Load the page index from disk, if it exists."""
        if not self.index_path.exists():
            return

        payload = json.loads(self.index_path.read_text(encoding="utf-8"))
        self.documents = payload.get("documents", [])
