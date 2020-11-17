from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from WebApp.models import Users
from .serializers import UsersSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from  rest_framework.authtoken.models import Token

class UserAuthentication(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token,created=Token.objects.get_or_create(user=user)
        return Response(token.key)

class UsersList(APIView):
    def get(self,request):
        model=Users.objects.all()
        serializer=UsersSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        model = Users.objects.all()
        serializer=UsersSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    def get(self, request, id):
        try:
            model = Users.objects.get(id=id)
        except Users.DoesNotExist:
            return Response(f"User with  id {id} Not Found",status=status.HTTP_204_NO_CONTENT)

        serializer = UsersSerializer(model)
        return Response(serializer.data)

    def put(self, request,id):
         model = Users.objects.get(id=id)
         serializer = UsersSerializer(model, data=request.data)
         if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,id):
         model = Users.objects.get(id=id)
         model.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)





