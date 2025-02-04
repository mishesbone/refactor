# refactor



```markdown
# Refactor: Content-to-Slides Converter

An AI-powered web app that converts text documents, PDFs, or spreadsheets into presentation slides. The app intelligently extracts and organizes key points from the input files and generates visually appealing slides. 

## Features
- Upload files in multiple formats: PDF, DOCX, TXT, CSV, and XLSX.
- AI-powered key point extraction using OpenAI's GPT.
- Automatically generates slides from the extracted content.
- Slide generation for various file types including PDF, Word, and more.
- Visualizations with Plotly for enhanced presentation.

## Tech Stack
- **Backend**: Python (Django)
- **Frontend**: HTML/CSS
- **AI**: OpenAI GPT (text-davinci-003 engine)
- **Visualization**: Plotly
- **File Processing**: PyPDF2, python-docx, pandas

## Installation

### Prerequisites:
- Python 3.8 or higher
- Django 3.x or higher
- OpenAI API Key (sign up on [OpenAI](https://beta.openai.com/signup/) for an API key)
- Install dependencies using pip

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/mishesbone/refactor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd refactor
   ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. Set the OpenAI API key as an environment variable (optional but recommended):
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

7. Run database migrations:
   ```bash
   python manage.py migrate
   ```

8. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

9. Navigate to `http://127.0.0.1:8000` in your web browser to access the app.

## File Uploads
The app supports the following file formats for uploads:
- **PDF**: Portable Document Format
- **DOCX**: Microsoft Word Document
- **CSV**: Comma-Separated Values
- **XLSX**: Excel Spreadsheet
- **TXT**: Plain Text Files

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to [OpenAI](https://openai.com/) for providing the GPT model.
- [Plotly](https://plotly.com/) for beautiful visualizations.
- [PyPDF2](https://pythonhosted.org/PyPDF2/) and [python-docx](https://python-docx.readthedocs.io/en/latest/) for handling document processing.

```

### Sections Included:
- **Project Overview**: Basic information about what the app does.
- **Features**: List of core functionalities.
- **Tech Stack**: Technologies used in the project.
- **Installation Instructions**: Step-by-step guide on setting up the environment and running the app.
- **Supported File Types**: Details on what file formats the app supports.
- **Contributing**: How others can contribute to the project.
- **License**: Information on the license (MIT is used here).
- **Acknowledgments**: Credits to the tools and libraries used in the project.

Make sure to customize the `OPENAI_API_KEY` setup, installation steps, and any other project-specific details before using the `README.md` for your repository!
