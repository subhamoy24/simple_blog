from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from user_profiles.serializer import UserProfileSerializer
from user_profiles.models import UserProfile

from user_profiles.serializer import UserSerializer

class ListUserProfile(APIView):
    def post(self, request, fomat=None):
        if "user" in request.data:
            try:
                user_profile = UserProfile.objects.get(user=request.data["user"])
                return Response({"msg": "user profile already created"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                pass

        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileDetail(APIView):
     def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.

        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404
    
     def patch(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        '''try:
            profile = UserProfile.objects.get(user=request.data["user"])
            if profile.id != user_profile.id:
                return Response({"msg": "unauthorized access"}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({"msg": "bad request"}, status=status.HTTP_400_BAD_REQUEST)'''
        
        print(request.data)
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
