from loader import loader

documents = loader("/home/blackpearl-/rag/documents")

print("Pages extracted:", len(documents))

for document in documents:
    print(f"\n{'=' * 60}")
    print("Source:", document["source"])
    print("Page:", document["page"])
    print("Characters:", len(document["text"]))
    print("=" * 60)
    print(document["text"][:1000])