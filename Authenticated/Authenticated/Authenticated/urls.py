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



from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),


    path(r'rest-auth/', include('rest_auth.urls'))

from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration', include('dj_rest_auth.registration.urls'))
>>>>>>> Aeesha:Feature: Included urls for registration and provided a doc.http with url calls to test that it is working fine

    path(r'rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration', include('dj_rest_auth.registration.urls'))
>>>>>>> Aeesha:Feature: Included urls for registration and provided a doc.http with url calls to test that it is working fine

from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'rest-auth/', include('dj_rest_auth.urls'))
>>>>>>> Reverted commit

from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
>>>>>>> Revert "@Hussain:djangoauth"
]

if getattr(settings, 'REST_USE_JWT', False):
    from rest_framework_simplejwt.views import (
        TokenRefreshView, TokenVerifyView,
    )

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]

    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration', include('dj_rest_auth.registration.urls'))
]

>>>>>>> Fixed issue with JWT


from django.urls import path
from django.contrib.auth import views as auth_views
from authentify import views as app_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html') , name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete'),
    path('index/', app_views.index ,name='password')
]
>>>>>>> marly:<Bug||Chore||Feature>:My Implementation of Forgot password(with mail support).
>>>>>>> Resolved merge conflict by incorporating both suggestions.
