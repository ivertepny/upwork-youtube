from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import VideoSearch
from .serializers import VideoSearchSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        return Response({'detail': 'User registered'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        searches = VideoSearch.objects.filter(user=request.user).order_by('-created_at')
        serializer = VideoSearchSerializer(searches, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
