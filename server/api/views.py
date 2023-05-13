from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    Users = User.objects.all()
    datalar = ItemSerializer(Users, many=True)
    return Response(datalar.data)