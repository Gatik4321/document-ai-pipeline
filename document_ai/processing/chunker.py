def chunk_text(text, chunk_size=1000, chunk_overlap=200):
    """
    Split text into overlapping chunks for processing.
    
    Args:
        text: The text to split
        chunk_size: Size of each chunk
        chunk_overlap: Overlap between chunks
        
    Returns:
        List of text chunks
    """
    chunks = []
    start = 0
    
    while start < len(text):
        # Get the end position for this chunk
        end = start + chunk_size
        
        # If this is not the last chunk, try to split at a sentence boundary
        if end < len(text):
            # Look for the last period, newline, or space before the end
            for separator in [". ", "\n", " "]:
                pos = text.rfind(separator, start + chunk_size // 2, end)
                if pos > start:
                    end = pos + len(separator)
                    break
        
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        
        # Move start position, accounting for overlap
        start = end - chunk_overlap
        
        # Prevent infinite loop
        if start >= len(text) - 1:
            break
    
    return chunks
