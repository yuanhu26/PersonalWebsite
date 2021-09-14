from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('contact.html', views.contact, name = "contact"),
    path('index.html', views.index, name = "index"),
    path('projects.html', views.projects, name = "projects"),
    path('resume.html', views.resume, name = "resume"),
    path('Projects/crypto_asset.html', views.crypto_asset, name = "crypto_asset")
    path('Projects/ETFs.html', views.ETFs, name = "ETFs")
    path('Projects/DJI30.html', views.ETFs, name = "DJI30")
]
