from PyPDF2 import PdfReader
from docx import Document


def extract_text(file_path):
    text = ""

    # Handle PDF files
    if file_path.lower().endswith(".pdf"):
        try:
            reader = PdfReader(file_path)

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        except Exception as e:
            return f"Error reading PDF: {str(e)}"

    # Handle DOCX files
    elif file_path.lower().endswith(".docx"):
        try:
            doc = Document(file_path)

            for para in doc.paragraphs:
                text += para.text + "\n"

        except Exception as e:
            return f"Error reading DOCX: {str(e)}"

    else:
        return "Unsupported file format"

    return text