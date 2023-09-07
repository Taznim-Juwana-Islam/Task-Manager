"""
URL configuration for Personal_Task_Manager project.

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
from django.conf import settings
from django.conf.urls.static import static
from Personal_Task_Manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', views.aboutus),
    path('user_registration/', views.user_registration),
    path('', views.login),
    path('task-creation/', views.task_creation),
    path('list/', views.list),
    path('details/', views.details),
    path('update/', views.update),
    path('task_deletion/', views.task_deletion),
    path('saveenquiry/',views.saveEnquiry,name="saveenquiry"),
    path('saveenquiry1/',views.saveEnquiry1,name="saveenquiry1"),
]

if settings.DEBUG:
    urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    