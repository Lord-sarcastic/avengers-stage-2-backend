from rest_framework import generics
from . import serializers
from ..authentify import models


class usernameauthentify(generics.ListCreateAPIView):
    queryset = models.Login.objects.all()
    serializer_class = serializers.LoginSerializer


class emailauthentify(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Login.objects.all()
    serializer_class = serializers.LoginSerializer


class passwordauthentify(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Login.objects.all()
    serializer_class = serializers.LoginSerializer
