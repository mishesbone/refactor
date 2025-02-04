def generate_slides(key_points):
    """
    Generates a list of slides from key points.

    Args:
        key_points (str): A string containing key points separated by newlines.

    Returns:
        list[dict]: A list of dictionaries representing slides with 'title' and 'content' fields.
    """
    if not key_points or not isinstance(key_points, str):
        raise ValueError("Key points must be a non-empty string.")

    slides = []
    points = [point.strip() for point in key_points.split('\n') if point.strip()]  # Clean and filter empty lines

    if not points:
        raise ValueError("No valid key points provided to generate slides.")

    for i, point in enumerate(points):
        slides.append({
            'title': f"Slide {i + 1}",
            'content': point
        })

    return slides
