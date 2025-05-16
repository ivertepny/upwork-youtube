from rest_framework import serializers
from .models import VideoSearch
from django.contrib.auth.models import User

class VideoSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSearch
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
