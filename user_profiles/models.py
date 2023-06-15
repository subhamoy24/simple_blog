from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  name = models.CharField(max_length=254, blank=False)
  email =  models.EmailField(max_length=254, unique=True)
  bio = models.TextField()
  profile_pic = models.ImageField(upload_to ='media/uploads/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)