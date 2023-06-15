from django.contrib import admin
from django.urls import path
from .views import ListUserProfile, UserProfileDetail

app_name = "user_profiles"
urlpatterns = [
    path('api/user-profiles', ListUserProfile.as_view(), name='user-profiles'),
    path('api/user-profiles/<int:pk>', UserProfileDetail.as_view(), name='user-profile-detail')
]