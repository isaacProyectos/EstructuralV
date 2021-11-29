from django.urls import path
from .views import calculaGrafo, umbral
from .views import procesamiento
#from .import views


urlpatterns = [
    path("mi-grafo/",calculaGrafo, name="grafo"),
    path("procesamiento/",procesamiento, name="procesamiento"),
    path("umb/",umbral, name="umbral"),

    
]