from django.shortcuts import render
from rest_framework.decorators import api_view
from guardar_imagenes.models import Imagenes
from guardar_imagenes.serialize import ImagenesSeralaizer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(["GET","DELETE","PUT"])
def get_image(request,id):
    image = Imagenes.objects.filter(id = id)
    
    if request.method == "GET":
        
        serializer = ImagenesSeralaizer(image, many=True) 

        return Response(serializer.data)
    elif request.method == "DELETE":
        serializer = ImagenesSeralaizer(image, many=True)   
        image.delete()
        return Response(serializer.data)

@api_view(["POST"])
def post_image(request):

    image = ImagenesSeralaizer(data = request.data)

    if image.is_valid():
        image.save()
        return Response(image.data, status=status.HTTP_201_CREATED)
    return Response(image.errors, status=status.HTTP_400_BAD_REQUEST)

