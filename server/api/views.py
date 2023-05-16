from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item 
from .serializers import ItemSerializer
from django.shortcuts import redirect


from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    datalar = ItemSerializer(items, many=True)
    return Response(datalar.data)

@api_view(['POST'])
def AddItems(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': username})
        else:
            return Response({'error': 'Invalid credentials'})
