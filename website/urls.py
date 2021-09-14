from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('contact.html', views.contact, name = "contact"),
    path('index.html', views.index, name = "index"),
    path('projects.html', views.projects, name = "projects"),
    path('resume.html', views.resume, name = "resume"),
    path('Projects/paper1.html', views.paper1, name = "paper1")
]
