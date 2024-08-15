import fitz  # PyMuPDF library 

def analyze_pdf(file_path):
    """Analyzes the text content of a PDF document and prints it page by page."""
    pdf_document = fitz.open(file_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")   

        print(f"Page {page_num + 1}:\n{text}\n{'-'*40}")

if __name__ == "__main__":
    pdf_file_path = "example.pdf"  # Update with the actual path to your PDF
    analyze_pdf(pdf_file_path)
