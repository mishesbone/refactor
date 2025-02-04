#app_slides/forms.py
from django import forms

class FileUploadForm(forms.Form):
    """Form for handling file uploads with supported file types."""
    file = forms.FileField(
        label='Select a file',
        help_text='Supported formats: PDF, DOCX, CSV, XLSX, TXT',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.pdf,.docx,.csv,.xlsx,.txt'
        })
    )
    title = forms.CharField(
        max_length=255,
        required=True,
        label='Slide Title',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a title for the slides'
        })
    )
    description = forms.CharField(
        max_length=500,
        required=False,
        label='Description',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a brief description (optional)',
            'rows': 3,
        })
    )
    file_type = forms.ChoiceField(
        choices=[
            ('pdf', 'PDF'),
            ('pptx', 'PowerPoint'),
            ('docx', 'Word'),
            ('txt', 'Text'),
            ('html', 'HTML'),
            ('csv', 'CSV'),
            ('xlsx', 'Excel'),
        ],
        required=True,
        label='File Type',
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )
