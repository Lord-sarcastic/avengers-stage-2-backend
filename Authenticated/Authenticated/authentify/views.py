from django.shortcuts import render


# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests, json
from django.shortcuts import HttpResponse


host = 'http://127.0.0.1:8000'



def test(request):
    r = requests.post(f'{host}/api/auth/register', data={"username":"Louisane", "password1":"MONKEYSex",
    "password2":"MONKEYSex", "email":"louis.paul9095@gmail.com"})
    return HttpResponse(r.json())


class RegistrationView(APIView):
    
    def post(self, request):
        r = requests.post(f'{host}/dj-rest-auth/registration/', data=request.POST)
        return HttpResponse(r.content)


class LoginView(APIView):
    
    def post(self, request):
        r = requests.post(f'{host}/dj-rest-auth/login/', data=request.POST)
        return HttpResponse(r.content)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        r = requests.post(f'{host}/dj-rest-auth/logout/')
        return Response(r.content)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        # return HttpResponse(json.dumps(content))
        return Response(content)


class ResetEmailView(APIView):
    def post(self, request):
        r = requests.post(f'{host}/dj-rest-auth/password/reset/', data=request.POST)
        return Response(r.content)

class ConfirmView(APIView):
    def get(self, request, uidb64, token):
        data = {'uid': uidb64, "token": token}
        return Response(data)


class ConfirmEmailView(APIView):
    def post(self, request):
        r = requests.post(f'{host}/dj-rest-auth/password/reset/confirm/', data=request.POST)
        return Response(r.content)


class UserView(APIView):
    
    def post(self, request):
        r = requests.post(f'{host}/dj-rest-auth/user/', data=request.POST)
        return Response(r.content)

    def get(self, request):
        r = requests.get(f'{host}/dj-rest-auth/user/', data=request.GET)
        return Response(r.content)

class VerifyEmailView(APIView):
    def get(self, request, key):
        r = requests.post(f'{host}/dj-rest-auth/registration/verify-email/', data={"key":key})
        return Response(r.content)