from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile(
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

