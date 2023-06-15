from django.test import TestCase

from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from user_profiles.models import UserProfile


class UserProfileAPITestCase(APITestCase):
    def test_user_profile_post(self):
        u = User.objects.create_user(username='john', email='jlennon@beatles.com', password='glass onion')
        with open('/home/subhamoy/simple_blog/media/uploads/Subhamoy_Das-8972053737.jpg', 'rb') as image_file:
            content = {"name": "subha", "email": "subha.das@gmail.com", "user_id": u.id, "profile_pic": image_file, "bio": "its me"}
            response = self.client.post('/user/api/user-profiles', content)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_profile_patch(self):
        u = User.objects.create_user(username='john', email='jlennon@beatles.com', password='glass onion')
        UserProfile.objects.create(name="subha", email="subha.das@gmail.com", user_id=u.id, bio="its me")
        response = self.client.patch(f'/user/api/user-profiles/{u.id}', {"name": "toy"})
        res = response.json()
        self.assertEquals(["name"], "toy")
        self.assertEquals(response.status_code, status.HTTP_200_OK)


        
        

