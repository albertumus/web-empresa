from django.urls import path
from . import views

urlpatterns = [
        #Path de los servicios
    path("services/", views.services, name="services"),

]