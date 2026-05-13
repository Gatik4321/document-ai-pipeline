class ReasoningPath:
    """Construct a reasoning path across retrieved pages."""

    def build_path(self, query, retrieved_pages):
        """Return a simple reasoning path for a query and matching pages."""
        path = []
        for document in retrieved_pages:
            path.append({
                "source": document["source"],
                "page": document["page"],
                "rationale": f"Page matches query terms from '{query}'.",
            })
        return path
