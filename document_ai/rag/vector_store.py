import faiss
import numpy as np

class VectorStore:
    """Vector store for semantic search using FAISS."""

    def __init__(self, dimension):
        """Initialize FAISS index."""
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add_documents(self, embeddings, documents):
        """Add documents and their embeddings to the store."""
        embeddings = np.array(embeddings).astype('float32')
        self.index.add(embeddings)
        self.documents.extend(documents)

    def search(self, query_embedding, k=5):
        """Search for similar documents."""
        query_embedding = np.array([query_embedding]).astype('float32')

        distances, indices = self.index.search(query_embedding, k)

        results = []
        for idx in indices[0]:
            results.append(self.documents[idx])

        return results
