import openai
from PyPDF2 import PdfReader
import docx
import pandas as pd

# OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_text(file):
    """Extracts text from supported file types."""
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
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return '\n'.join([p.text for p in doc.paragraphs])

def extract_text_from_spreadsheet(file):
    df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
    return df.to_string()

def extract_key_points(text):
    """Uses OpenAI GPT to extract key points from text."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Extract key points from the following text:\n{text}",
        max_tokens=300
    )
    return response.choices[0].text.strip()
