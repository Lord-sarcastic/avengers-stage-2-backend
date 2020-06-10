from django.shortcuts import render


# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests, json
from django.shortcuts import HttpResponse


host = 'http://127.0.0.1:8000'



def test(request):
    url = 'http://127.0.0.1:8000/api/auth/login'
    # headers = {"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ1MjI0MjAwLCJqdGkiOiJlMGQxZDY2MjE5ODc0ZTY3OWY0NjM0ZWU2NTQ2YTIwMCIsInVzZXJfaWQiOjF9.9eHat3CvRQYnb5EdcgYFzUyMobXzxlAVh_IAgqyvzCE"}

    r = requests.post(url, data={'email':'louis.paul9095@gmail.com','password':'MONKEYSex9095'})
    # print(r.json())
    # access = r.json()['access_token']
    # username = r.json()['user']['username']
    # print(username)
    # visit = requests.get(f'{host}/api/auth/user', 
    # params={"username": username,"first_name":"", "last_name":""})
    # visit = requests.get(f'{host}/reset/MQ/5h8-8448e71688a6009ded47/')
    # data = visit.json()
    # data['new_password1'] = 'MONKEYSex9095'
    # data['new_password2'] = 'MONKEYSex9095'
    # r = requests.post(f'{host}/api/auth/confirm', data=data)
    return HttpResponse(r.content)



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