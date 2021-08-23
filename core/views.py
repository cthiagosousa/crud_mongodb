from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import AccountSerializer

User = get_user_model()

class AccountViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer

    def account_details(self, request: HttpRequest, pk: str) -> Response:
        try:
            account = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'})

        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
    def create(self, request: HttpRequest) -> Response:
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    def update(self, request: HttpRequest, pk: str) -> Response:
        try:
            account = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response({'error': 'Usuário não encontrado'})
        
        serializer = AccountSerializer(account, request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Usuário atualizado'})
        
        return Response({serializer.errors})

    def destroy(self, request: HttpRequest, pk: str):
        User.objects.delete(id=pk)

        return Response({'success': 'Usuário deletado.'})
