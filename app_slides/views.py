from django.shortcuts import render
from .ai_processing.content_parser import extract_text, extract_key_points
from .ai_processing.slide_generator import generate_slides
from .data_visualization.plot_generator import create_visualization
import pandas as pd

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        try:
            text = extract_text(file)
            key_points = extract_key_points(text)
            slides = generate_slides(key_points)
            
            # For spreadsheet data visualization
            if file.name.endswith('.csv') or file.name.endswith('.xlsx'):
                data = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
                visualization = create_visualization(data)
            else:
                visualization = None

            return render(request, 'slides.html', {'slides': slides, 'visualization': visualization})
        except Exception as e:
            return render(request, 'upload.html', {'error': str(e)})
    return render(request, 'upload.html')
