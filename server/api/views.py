from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth import authenticate

@api_view(['GET'])
def getData(request):
    return ""
    # items = Item.objects.all()
    # datalar = ItemSerializer(items, many=True)
    # return Response(datalar.data)

class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': username})
        else:
            return Response({'error': 'Kullanıcı adı veya parola hatalı'})