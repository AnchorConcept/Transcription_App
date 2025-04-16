from django.urls import path
from .views import TranscriptionListCreateView

urlpatterns = [
    path(
        '',
        TranscriptionListCreateView.as_view(),
        name='transcription-list-create',
    ),
]
