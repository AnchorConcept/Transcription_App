from django.db import models
from django.contrib.auth.models import User


class Transcription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    transcript_text = models.TextField()
    audio_file = models.FileField(
        upload_to='transcriptions/', null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
