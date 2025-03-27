"""Download_videos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from link_collector import views
from link_collector.views import collector
from regform.views import index_1, congrat, login_page
from link_collector.views import form1_view, form2_view
from youtube_links_api.views import protected_view, ProtectedAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_1),
    path('login/', login_page),
    path('congrat/', congrat),
    path('collector/', collector),
    path('form1/', views.form1_view, name='form1_view'),
    path('form2/', views.form2_view, name='form2_view'),
    path('admin/', admin.site.urls),
    path('api/', include('youtube_links_api.urls')),
    path('links/', include('frontend.urls')),
    path('api/protected/', protected_view, name='protected_view'),
    path('api/protected-cbv/', ProtectedAPIView.as_view(), name='protected_cbv'),
]
