from pathlib import Path
from pypdf import PdfReader
def loader(directory):
    documents = []
    for path in Path(directory).glob("*.pdf"):
        reader = PdfReader(path)
        for page_n,page in enumerate(reader.pages,start=1):
            text = page.extract_text() or " "
            if text.strip():
                documents.append({
                "text" : text,
		        "source" : page_n,
		        "page" : path.name
})
    return documents


