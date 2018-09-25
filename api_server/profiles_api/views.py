from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    # model = models.UserProfile
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication, )
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'last_name', 'email')


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return  ObtainAuthToken().post(request)