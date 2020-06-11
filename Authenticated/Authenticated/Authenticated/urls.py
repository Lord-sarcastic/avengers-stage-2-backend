"""Authenticated URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from authentify.views import ConfirmView, VerifyEmailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', RegisterView.as_view(), name="register"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('dj-rest-auth/registration/account-confirm-email/<key>/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('api/auth/', include('authentify.urls')),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
     url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        ConfirmView.as_view(), name='password_reset_confirm'),
    url('^', include('django.contrib.auth.urls'))

]
