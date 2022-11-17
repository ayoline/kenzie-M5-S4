from rest_framework import generics
from .models import Account
from .serializers import RegisterSerializer


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer


class AccountUpdateView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer
    lookup_url_kwarg = "user_id"
