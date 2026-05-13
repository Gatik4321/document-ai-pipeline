import re

class HierarchicalRetriever:
    """Simple page-level retriever based on term overlap."""

    def retrieve(self, query, page_index_store, k=5):
        query_terms = set(re.findall(r"\w+", query.lower()))
        if not query_terms:
            return []

        scored = []
        for document in page_index_store.documents:
            text = document.get("text", "").lower()
            score = sum(text.count(term) for term in query_terms)
            if score > 0:
                scored.append((score, document))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [doc for _, doc in scored[:k]]
