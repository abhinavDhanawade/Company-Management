from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from management.models import Employe
from empapi.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.

class TaskAPIView(APIView):

    def get(self, request):
        details = Employe.objects.all()
        serializer = TaskSerializer(details, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeDetailsAPIView(APIView):

    def get_object(self, id):
        try:
            return Employe.objects.get(empId=id)
        except Employe.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        details = self.get_object(id)
        serializer = TaskSerializer(details)
        return Response(serializer.data)

    def put(self, request, id):
        details = self.get_object(id)
        serializer = TaskSerializer(details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        details = self.get_object(id)
        details.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)