from django.urls import path
from guardar_imagenes.views import get_image, post_image

urlpatterns = [
    path('ima/<int:id>', get_image ),
    path('ima/', post_image),
]