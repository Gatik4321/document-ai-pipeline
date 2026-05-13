from pyvis.network import Network
import os

def visualize_graph(graph, output_file="knowledge_graph.html"):
    """Visualize knowledge graph using PyVis."""
    try:
        net = Network(
            notebook=False,
            height="750px",
            width="100%",
            directed=False
        )

        net.from_nx(graph)
        
        # Configure physics simulation
        net.physics = True
        net.toggle_physics(True)
        
        # Save HTML file directly
        net.write_html(output_file, notebook=False)
        
        print(f"✓ Knowledge graph visualization saved to {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"Warning: Could not generate interactive visualization: {str(e)}")
        # Fallback: Create a simple graph representation
        print(f"Graph contains {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges")

