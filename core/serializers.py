from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password_confirm', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}
    
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    is_staff = serializers.BooleanField(
        label="Membro da Equipe",
        help_text="Indica que usuário consegue acessar o site de administração."
    )

    is_superuser = serializers.BooleanField(
        label="SuperUsuário",
        help_text="Indica que este usuário tem todas as permissões sem atribuí-las explicitamente."
    )

    def save(self) -> User:
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']
        is_staff = self.validated_data['is_staff']
        is_superuser = self.validated_data['is_superuser']

        if password != password_confirm:
            raise serializers.ValidationError({'error': 'As senhas não são iguais'})
        
        account = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser
        )

        return account
