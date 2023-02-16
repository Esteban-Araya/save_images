from guardar_imagenes.models import Imagenes
from rest_framework import serializers

class ImagenesSeralaizer(serializers.ModelSerializer):

    class Meta:
        model = Imagenes
        fields = "__all__"
