from ingest import load_documents

docs = load_documents("campus_life")
lengths = []
for doc in docs:
    paragraphs = [p.strip() for p in doc.text.split("\n\n") if p.strip()]
    lengths.extend(len(p) for p in paragraphs)

lengths.sort()
def is_heading_like(paragraph: str) -> bool:
    return not any(p in paragraph for p in ".?!")

for doc in docs:
    paragraphs = [p.strip() for p in doc.text.split("\n\n") if p.strip()]
    for p in paragraphs:
        if is_heading_like(p) and len(p) > 60:
            print("FALSE POSITIVE?", p)   # long paragraph flagged as heading — check it