from base.models import Item, Blog
from .serializers import ItemSerializer, UserSerializer
from django.shortcuts import redirect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
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


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserBlogsAPIView(APIView):
    def get(self, request, format=None):
        user = request.user
        blogs = Blog.objects.filter(user=user)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


