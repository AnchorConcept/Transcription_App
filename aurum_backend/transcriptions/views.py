from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Transcription
from .serializers import TranscriptionSerializer

 
class TranscriptionListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        transcriptions = Transcription.objects.filter(user=request.user)
        serializer = TranscriptionSerializer(transcriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TranscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
