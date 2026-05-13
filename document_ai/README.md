# Enterprise Document Intelligence Pipeline (POC)

A comprehensive document processing system that ingests PDFs, extracts text, creates embeddings, builds knowledge graphs, and enables semantic search.

## Features

- **Open Data Loader**: Structured PDF extraction to page-level JSON/Markdown
- **Page Index**: Page mapping and metadata storage for efficient retrieval
- **Embeddings**: Generate embeddings using sentence-transformers
- **Vector Search**: FAISS-based semantic retrieval
- **Entity Extraction**: Extract entities using spaCy
- **Knowledge Graph**: Build dynamic graphs from extracted entities
- **Graph Visualization**: Interactive HTML visualization using PyVis
- **Cross-document Insights**: Identify overlapping entities and relationships

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

2. Add PDF files to the `data/pdfs/` folder

3. Run the pipeline:
```bash
python main.py
```

## Project Structure

```
document_ai/
├── data/
│   └── pdfs/                    # Place PDF files here
├── ingestion/
│   ├── open_dataloader_ingest.py # Page-level Open Data Loader extraction
│   ├── pdf_loader.py            # PDF text extraction
│   └── ocr_engine.py            # OCR for scanned PDFs (future)
├── page_index/                  # Page index and retrieval helpers
│   ├── page_index_store.py      # Page metadata and mapping storage
│   ├── semantic_tree_builder.py # Page-level semantic tree builder
│   ├── hierarchical_retriever.py# Simple page retriever
│   └── reasoning_path.py        # Lightweight reasoning path generator
├── processing/
│   ├── chunker.py               # Text chunking
│   └── embeddings.py            # Embedding generation
├── graph/
│   ├── entity_extractor.py      # Named entity extraction
│   └── graph_builder.py         # Knowledge graph construction
├── rag/
│   └── vector_store.py          # Vector search implementation
├── visualization/
│   └── visualize_graph.py       # Graph visualization
├── main.py                      # Main pipeline
└── requirements.txt             # Dependencies
```

## Outputs

After running the pipeline, you'll get:

1. **knowledge_graph.html**: Interactive graph visualization (open in browser)
2. **Vector Store**: In-memory FAISS index for semantic search
3. **Console Output**: Processing logs and statistics

## System Capabilities

| Feature | Status |
|---------|--------|
| Large PDF ingestion | ✓ |
| Semantic chunking | ✓ |
| Embeddings | ✓ |
| Vector Search | ✓ |
| Entity Extraction | ✓ |
| Graph Generation | ✓ |
| Cross-document overlap | ✓ |
| Visualization | ✓ |

## Next Level Improvements

### 1. Neo4j Integration
Replace NetworkX with Neo4j for enterprise-grade graph database capabilities.

### 2. Advanced OCR
Use PaddleOCR for scanned PDF documents.

### 3. GraphRAG Implementation
Enable graph-based retrieval augmented generation for LLM integration.

### 4. Overlapping Insights Detection
Automatically detect and link related entities across documents.

### 5. Automatic Summaries
Generate chunk summaries using LLMs and store in graph nodes.

### 6. Metadata Tracking
Store page numbers, sections, source PDFs, and confidence scores.

## Key Technologies

- **PyPDF2**: Open-source PDF text extraction by page
- **Sentence-Transformers**: Embeddings (all-MiniLM-L6-v2)
- **FAISS**: Vector similarity search
- **NetworkX**: Knowledge graph construction
- **spaCy**: Named entity recognition
- **LangChain**: Text processing utilities
- **PyVis**: Interactive graph visualization
- **NumPy & Pandas**: Data processing

## Usage Example

```python
from ingestion.pdf_loader import extract_text_from_pdf
from processing.chunker import chunk_text
from processing.embeddings import create_embeddings

# Load and process
text = extract_text_from_pdf("document.pdf")
chunks = chunk_text(text)
embeddings = create_embeddings(chunks)

# Search
from rag.vector_store import VectorStore
vector_store = VectorStore(dimension=384)
vector_store.add_documents(embeddings, chunks)
results = vector_store.search(query_embedding, k=5)
```

## Manager Pitch

"I have designed a scalable document intelligence pipeline that ingests large PDFs, performs semantic chunking and embedding generation, extracts entities and relationships, and builds a dynamic knowledge graph for cross-document insight discovery. The system also supports vector retrieval and graph-based semantic reasoning for future GraphRAG integration."

---

**Version**: 0.1.0  
**Status**: Proof of Concept
