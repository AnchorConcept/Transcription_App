from rest_framework import serializers
from .models import Transcription


class TranscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcription
        fields = [
            'id', 
            'user', 
            'title', 
            'transcript_text', 
            'audio_file', 
            'created_at'
        ]
        read_only_fields = ['id', 'user', 'created_at']