#app_slides/ai_processing/__init__.py

"""
AI Processing Module.

This module contains functionalities for processing content
and generating slides using AI-powered tools.
"""

from .content_parser import extract_text, extract_key_points
from .slide_generator import generate_slides

__all__ = [
    "extract_text",
    "extract_key_points",
    "generate_slides",
]
