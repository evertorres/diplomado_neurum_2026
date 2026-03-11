import fitz
import sys

def extract_pdf_text(filepath):
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text() + "\n\n--- PAGE BREAK ---\n\n"
    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_text.py <pdf_path>")
        sys.exit(1)
        
    path = sys.argv[1]
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(extract_pdf_text(path))
    print("Done")
