def generate_slides(key_points):
    """Generates a dictionary of slides from key points."""
    slides = []
    points = key_points.split('\n')
    for i, point in enumerate(points):
        slides.append({
            'title': f"Slide {i + 1}",
            'content': point.strip()
        })
    return slides
