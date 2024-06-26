from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from base.serializer import  UserSerializer, UserSerializerwithToken


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerwithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getUserProfile(request):

    # op = {product['_id']: product for product in products}
    # product_found = (op.get(pk))
    user = request.user
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)

@api_view(['GET'])
def updateUserProfile(request):

    # op = {product['_id']: product for product in products}
    # product_found = (op.get(pk))
    user = request.user
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def registerUsers(request):

    data = request.data

    try:
        user = User.objects.create(first_name=data['name'],
                                   username=data["email"],
                                   email=data["email"],
                                   password=make_password(data['password'])

                                   )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    except:

        message = {'detail': 'User with email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


 
