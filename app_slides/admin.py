from django.contrib import admin
from .models import Slide

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    """Admin configuration for the Slide model."""
    list_display = ('title', 'file_type', 'created_at', 'updated_at')
    list_filter = ('file_type', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'file_type', 'file_path')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
