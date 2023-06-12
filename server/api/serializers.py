from rest_framework import serializers
from base.models import Item, CustomUser, Blog
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['usefrname'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
