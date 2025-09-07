from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'age', 'email', 'phone', 'date_joined')

class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255, write_only = True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'age', 'email', 'phone', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':'Пароли не совпадают!'})
        
        if '+996' not in attrs['phone']:
            raise serializers.ValidationError({'phone':'Введенный номер не соответствует стандартам КР. Пример: +996-ХХХ-ХХ-ХХ-ХХ'})
        
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            age = validated_data['age'],
            email = validated_data['email'],
            phone = validated_data['phone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user