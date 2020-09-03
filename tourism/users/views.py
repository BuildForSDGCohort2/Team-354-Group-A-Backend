from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from .serializers import userSerializer, userpropertiesserializer
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
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
            token = Token.objects.get(user=user).key
            data["token"] = token

        else:
            data = serializer.errors
            return Response(data)
        return Response(data)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def userdetails(request):
    try:
        user = request.user
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = userpropertiesserializer(user)
        return Response(serializer.data)


@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def updateuser(request):
    try:
        user = request.user
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = userpropertiesserializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["response"] = "account update successfully"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
