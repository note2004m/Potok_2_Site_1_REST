from django.urls import path

from apps.users.views import UserAPIView, UserCreateAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user_api'),
    path('create_user/', UserCreateAPIView.as_view(), name='user_create_api'),
    path('detail_user/<int:pk>', UserDetailAPIView.as_view(), name='user_detail_api'),
    path('update_user/<int:pk>', UserUpdateAPIView.as_view(), name='user_update_api'),
    path('delete_user/<int:pk>', UserDeleteAPIView.as_view(), name='user_delete_api'),
]