from django.urls import path

from apps.users.views import UserAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user_api')
]