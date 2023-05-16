from rest_framework import serializers
from base.models import Item
from rest_framework.authtoken.models import Token



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'