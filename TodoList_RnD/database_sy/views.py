# from django.shortcuts import render
from database_sy.models import table_yy
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ReactSerializer
# Create your views here.

class storage(APIView):

    def get(self, request):
        output = [{
            "username": output.username,
            "passward": output.passward
        } for output in table_yy.objects.all()]

        return Response(output)


    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

