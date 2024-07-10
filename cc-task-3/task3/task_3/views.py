from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *


class uploadapi(APIView):
    def post(self,request):
        file = request.FILES.get('file')
        
        if not file:
            return Response(
                {
                    "message":"Please upload a file"
                },
                status= status.HTTP_400_BAD_REQUEST
            )
        filename = str(file)
        content = bytes(file.read())

        newfileobj = task(file_name = filename,content= content)
        newfileobj.save()
        return Response(
            {
                "message":"file uploaded successfuly"
            },
            status= status.HTTP_200_OK
        )


class retrievedata(APIView):
    def get(self,request,filename):
        taskobj = task.objects.filter(file_name = filename).first()
        if not taskobj:
            return Response(
                {
                    "message":"No such file found",
                },
                status=status.HTTP_400_BAD_REQUEST

            )  
        return Response(
            data = taskobj.content.tobytes().decode("utf8"),
            status= status.HTTP_200_OK
        )


class removefile(APIView):
    def get(self,reqiest,filename):
        taskobj = task.objects.filter(file_name = filename)
        if not taskobj:
            return Response(
                {
                    "message":"No such file found"
                },
                status=status.HTTP_400_BAD_REQUEST

            )  
        taskobj.delete()
        return Response(
            {
                "message":"files deleted"
            },
            status= status.HTTP_200_OK
        )


