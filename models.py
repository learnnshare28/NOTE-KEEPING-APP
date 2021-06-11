from django.db import models
from ckeditor.fields import RichTextField


class Task(models.Model):
    note_title = models.CharField(max_length=30)
    note_description = RichTextField(blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note_title
