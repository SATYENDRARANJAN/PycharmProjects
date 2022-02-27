from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import InsurerSerializer,LoginUserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Create your views here.
class UserCreate(APIView):
    # create the user
    def post(self, request, format='json'):
        serializer = InsurerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUser(APIView):
    def post(self,request,format='json'):
        serializer =LoginUserSerializer(data =request.data)
        user = serializer.validated_data
        if serializer.is_valid():
            token= Token.objects.create(user= user)
            json = user
            json['token'] = token.key
            return Response(
                json,status =status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user