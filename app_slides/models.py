#app_slides/modesl.py
from django.db import models

# Create your models here.
class Slide(models.Model):
    """Model for slides."""
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file_type = models.CharField(
        max_length=10,
        choices=[
            ('pdf', 'PDF'),
            ('pptx', 'PowerPoint'),
            ('docx', 'Word'),
            ('txt', 'Text'),
            ('html', 'HTML'),
            ('csv', 'CSV'),
            ('xlsx', 'Excel'),
        ]
    )
    file_path = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Slides"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.file_type})"
