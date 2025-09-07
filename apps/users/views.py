from rest_framework.generics import ListAPIView

from apps.users.models import User
from apps.users.serializers import UserSerializer

# Create your views here.
class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer