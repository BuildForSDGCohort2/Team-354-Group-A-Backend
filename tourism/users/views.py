from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import userSerializer

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = userSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()            
            data["email"] = user.email
            data["first_name"] = user.first_name
            data["last_name"] = user.last_name
            data["phone_number"] = user.phone_number
            
        else:
            data = serializer.errors
            return Response(data)
        return Response(data)
    

