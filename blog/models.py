from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import os
from django_prose_editor.fields import ProseEditorField

    

class Category(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True
        )
    slug = models.SlugField(
        unique=True
        )

    def __str__(self):
        return self.name



class Post(models.Model):

    title = models.CharField(
        max_length=200,
        help_text="Enter the title of the blog post."
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="Unique URL-friendly identifier for the post."
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        help_text="Author of the blog post."
    )

    content = ProseEditorField(
        sanitize=True,
        extensions={
            # Core text formatting
            "Bold": True,
            "Italic": True,
            "Strike": True,
            "Underline": True,
            "HardBreak": True,

            # Structure
            "Heading": {
                "levels": [1, 2, 3,4,5,6]  # Only allow h1, h2, h3
            },
            "BulletList": True,
            "OrderedList": True,
            "Blockquote": True,

            # Advanced extensions
            "Link": {
                "enableTarget": True,  # Enable "open in new window"
                "protocols": ["http", "https", "mailto"],  # Limit protocols
            },
            "Table": True,

            # Editor capabilities
            "History": True,       # Enables undo/redo
            "HTML": True,          # Allows HTML view
            "Typographic": True,   # Enables typographic chars
        }
    )

    created = models.DateTimeField(
        auto_now_add=True,
        help_text="Time when the post was first created."
    )

    updated = models.DateTimeField(
        auto_now=True,
        help_text="Time when the post was last updated."
    )

    published = models.DateTimeField(
        default=timezone.now,
        help_text="Time when the post is published."
    )

    caption = models.CharField(
        max_length=255,
        help_text="Enter the caption.",
        blank=False,
        null=True,
        )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="posts"
        )

    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True
        )
    
    class Meta:
        ordering = ['-published']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Check if an image exists and delete it
        if self.image:
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        
        # Proceed with deleting the model instance
        super().delete(*args, **kwargs)

	
