from django.urls import path
from .views import Home, Services
from . import views

app_name = 'home'
urlpatterns = [
    path("", views.Home, name="home"),
    path("projects/<str:slug>", views.project_details, name="project-details"),
    path("services/<str:slug>", views.singl_service, name="single-service"),

]
