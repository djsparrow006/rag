from loader import loader
from chunker import chunker

documents = loader("/home/blackpearl-/rag/documents")

all_chunks = []

for document in documents:
    chunks = chunker(document["text"])

    for index, chunk in enumerate(chunks):
        all_chunks.append({
            "text": chunk,
            "source": document["source"],
            "page": document["page"],
            "chunk_index": index
        })

print("Pages loaded:", len(documents))
print("Chunks created:", len(all_chunks))

for chunk in all_chunks[:3]:
    print("\nSource:", chunk["source"])
    print("Page:", chunk["page"])
    print("Chunk index:", chunk["chunk_index"])
    print("Text preview:", chunk["text"][:150])