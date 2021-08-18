from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers import AccountSerializer

User = get_user_model()

class AccountViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
