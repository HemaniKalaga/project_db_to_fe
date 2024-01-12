"""
URL configuration for project_db_to_fe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/',author,name='author'),
    path('book/',book,name='book'),
    path('student/',student,name='student'),
    path('insert_author/',insert_author,name='insert_author'),
    path('insert_book/',insert_book,name='insert_book'),
    path('insert_student/',insert_student,name='insert_student'),
    path('display_all/',display_all,name='display_all'),
    path('update_student/',update_student,name='update_student'),
]
