from sentence_transformers import SentenceTransformer

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(chunks):
    """Generate embeddings for text chunks."""
    embeddings = model.encode(chunks)

    return embeddings
