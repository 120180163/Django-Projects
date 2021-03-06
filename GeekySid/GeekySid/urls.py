"""GeekySid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('emailer', views.emailer, name='emailer'),
    path('bookstore/', include('bookstore.urls')),
    path('octaprofile/', include('octaprofile.urls')),
    path('scorebuzz/', include('scorebuzz.urls')),
    path('riddlechamp/', include('RiddleChamp.urls')),
    path('account/', include('Account.urls')),
    path('instagramscraper/', include('instagramscraper.urls'))
]

url_static = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
url_media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + url_static + url_media
