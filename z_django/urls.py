"""z_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from zboard import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.login_user, name="login"),
    path("", views.home, name="home"),
    path("meds/", include("meds.urls")),
    path("mar/", include("mar.urls")),
    path("bm/", include("bm.urls")),
    path("equipment/", include("equipment.urls")),
    path("notes/", include("notes.urls")),
    path('seizure/', include('seizure.urls')),
    path('interventions/', include('interventions.urls'))
    
]
