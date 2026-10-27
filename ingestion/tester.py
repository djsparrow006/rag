from loader import loader

documents = loader("/home/blackpearl-/rag/documents")

print("Pages loaded:", len(documents))

for document in documents[:3]:
    print("\nSource:", document["source"])
    print("Page:", document["page"])
    print("Text preview:", document["text"][:200])
