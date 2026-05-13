import networkx as nx

class KnowledgeGraph:
    """Build and manage knowledge graphs from extracted entities."""

    def __init__(self):
        """Initialize the knowledge graph."""
        self.graph = nx.Graph()

    def add_entities(self, entities, document_name):
        """Add entities and their relationships to the graph."""
        for entity in entities:
            node = entity["text"]

            self.graph.add_node(
                node,
                label=entity["label"]
            )

            self.graph.add_edge(
                document_name,
                node
            )

    def get_graph(self):
        """Return the knowledge graph."""
        return self.graph
