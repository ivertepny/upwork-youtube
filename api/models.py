from django.db import models
from django.contrib.auth.models import User

class VideoSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
