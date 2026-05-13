class SemanticTreeBuilder:
    """Build a semantic tree over page-level content."""

    def build(self, page_documents):
        """Create a lightweight semantic structure from page content."""
        tree = []

        for doc in page_documents:
            tree.append({
                "source": doc["source"],
                "page": doc["page"],
                "summary": doc["text"][:200],
            })

        return tree
