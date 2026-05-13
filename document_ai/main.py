import os

from ingestion.open_dataloader_ingest import load_pdf_pages, save_extracted_pages
from processing.embeddings import create_embeddings
from page_index.page_index_store import PageIndexStore
from rag.vector_store import VectorStore
from graph.entity_extractor import extract_entities
from graph.graph_builder import KnowledgeGraph
from visualization.visualize_graph import visualize_graph

# Base project directories for input PDFs and stored metadata
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_FOLDER = os.path.join(BASE_DIR, "data", "pdfs")
METADATA_FOLDER = os.path.join(BASE_DIR, "data", "metadata")


def main():
    """Run the complete document intelligence pipeline."""

    # Storage for page-level documents and their vector embeddings
    all_documents = []
    all_embeddings = []

    # Build a knowledge graph from extracted entities
    knowledge_graph = KnowledgeGraph()

    # Ensure PDF input folder exists before starting
    if not os.path.exists(PDF_FOLDER):
        print(f"Error: {PDF_FOLDER} folder not found")
        return

    # Collect all PDF files in the input folder
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]
    if not pdf_files:
        print(f"No PDF files found in {PDF_FOLDER}")
        return

    # Initialize page index storage for page metadata
    page_index = PageIndexStore(METADATA_FOLDER)

    for file in pdf_files:
        pdf_path = os.path.join(PDF_FOLDER, file)
        print(f"Processing: {file}")

        try:
            # 1) Extract text from each PDF page
            page_documents = load_pdf_pages(pdf_path)
            if not page_documents:
                print(f"⚠️ No text extracted from {file}")
                continue

            # 2) Save extracted page data as structured JSON/Markdown
            extracted_paths = save_extracted_pages(pdf_path, page_documents)
            print(f"  - extracted to: {extracted_paths['json']}")

            # 3) Generate embeddings for each extracted page text
            page_texts = [page["text"] for page in page_documents]
            embeddings = create_embeddings(page_texts)

            # 4) Add page documents and embeddings to memory
            all_documents.extend(page_documents)
            all_embeddings.extend(embeddings)

            # 5) Add page metadata to the page index
            page_index.add_documents(page_documents)

            # 6) Extract named entities from the combined page text
            entities = extract_entities("\n".join(page_texts))

            # 7) Add these entities to the knowledge graph
            knowledge_graph.add_entities(entities, file)
            print(f"✓ Completed: {file} ({len(page_documents)} pages, {len(entities)} entities)")

        except Exception as e:
            print(f"✗ Error processing {file}: {str(e)}")

    # 8) Save the page index file to disk
    index_path = page_index.save()
    print(f"\n✓ Page index saved to {index_path}")

    # 9) Build the vector store for semantic search
    if all_embeddings:
        dimension = len(all_embeddings[0])
        vector_store = VectorStore(dimension)
        vector_store.add_documents(all_embeddings, all_documents)
        print(f"\n✓ Vector store created with {len(all_documents)} page entries")

        # 10) Create graph visualization output
        graph = knowledge_graph.get_graph()
        visualize_graph(graph)
        print("✓ Knowledge graph visualization saved to knowledge_graph.html")
        print("\nPipeline Completed Successfully!")
    else:
        print("No embeddings generated. Check if PDFs contain text.")


if __name__ == "__main__":
    main()
