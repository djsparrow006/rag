def chunker(documents,chunk_size=500,over_lap=50):
    if chunk_size <=0:
        raise ValueError("chunk_size must be greater than 0")
    if over_lap < 0:
        raise ValueError("overlap must be greater than or equal to zero")
    chunks = []
    start = 0
    while start < len(documents):
        end = start+chunk_size
        chunk = documents[start:end]
        if chunk.strip():
            chunks.append(chunk)
        start += chunk_size - over_lap
    return chunks

