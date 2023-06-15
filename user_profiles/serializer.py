from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=False, max_length=254)
    email = serializers.EmailField(allow_blank = False, max_length=254)
    profile_pic = serializers.ImageField()
    bio = serializers.CharField()
    user_id = serializers.IntegerField()

    class Meta:
        model = UserProfile
    
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.user_id = validated_data.get('user_id', instance.user_id)

        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField(allow_blank = False, max_length=254)
