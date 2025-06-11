from PyPDF2 import PdfReader

def extract_text_by_page(file):
    """Extract text page-by-page and return as a list."""
    pdf_reader = PdfReader(file)
    pages = []
    for i, page in enumerate(pdf_reader.pages):
        content = page.extract_text() or ""
        pages.append({"text": content, "page": i + 1})
    return pages
