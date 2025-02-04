#app_slides/ai_processing/content_parser.py
import openai
from PyPDF2 import PdfReader
import docx
import pandas as pd

# OpenAI API key
# Ensure this is securely managed via environment variables
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text(file):
    """
    Extracts text from supported file types.

    Args:
        file (UploadedFile): The uploaded file to extract text from.

    Returns:
        str: Extracted text content from the file.

    Raises:
        ValueError: If the file type is unsupported.
    """
    if file.name.endswith('.pdf'):
        return extract_text_from_pdf(file)
    elif file.name.endswith('.docx'):
        return extract_text_from_docx(file)
    elif file.name.endswith('.csv') or file.name.endswith('.xlsx'):
        return extract_text_from_spreadsheet(file)
    elif file.name.endswith('.txt'):
        return file.read().decode('utf-8')
    else:
        raise ValueError("Unsupported file type.")

def extract_text_from_pdf(file):
    """
    Extracts text from a PDF file.

    Args:
        file (UploadedFile): The PDF file to extract text from.

    Returns:
        str: Text extracted from the PDF.
    """
    try:
        reader = PdfReader(file)
        text = ''.join(page.extract_text() for page in reader.pages if page.extract_text())
        return text.strip()
    except Exception as e:
        raise ValueError(f"Error reading PDF file: {e}")

def extract_text_from_docx(file):
    """
    Extracts text from a Word document (.docx).

    Args:
        file (UploadedFile): The Word document file.

    Returns:
        str: Extracted text content from the Word document.
    """
    try:
        doc = docx.Document(file)
        return '\n'.join(p.text for p in doc.paragraphs if p.text).strip()
    except Exception as e:
        raise ValueError(f"Error reading Word document: {e}")

def extract_text_from_spreadsheet(file):
    """
    Extracts text from a spreadsheet (CSV or Excel).

    Args:
        file (UploadedFile): The spreadsheet file.

    Returns:
        str: String representation of the spreadsheet content.
    """
    try:
        df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
        return df.to_string(index=False)
    except Exception as e:
        raise ValueError(f"Error reading spreadsheet: {e}")

def extract_key_points(text):
    """
    Uses OpenAI GPT to extract key points from the provided text.

    Args:
        text (str): The text to summarize into key points.

    Returns:
        str: Key points extracted from the text.

    Raises:
        ValueError: If OpenAI fails to generate a response.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Extract key points from the following text:\n{text}",
            temperature=0.5,
            max_tokens=300,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise ValueError(f"Error with OpenAI API: {e}")
