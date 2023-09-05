"""
URL configuration for Netflix project.

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
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # newbie links
    path('home/',home,name='home'),
    path('join/',join,name='join'),
    path('enter/',enter,name='enter'),
    path('clear/',clear,name='clear'),
    # logged in user urls 
    path('exit/',exit,name='exit'),
    path('replace/',replace,name='replace'),
    path('expose/',expose,name='expose'),
    # Video links
    path('tiger/',tiger,name='tiger'),
    path('antony/',antony,name='antony'),
    path('wednesday/',wednesday,name='wednesday'),
    path('japan/',japan,name='japan'),
    path('og/',og,name='og'),
    # Genres
    path('movies/',movies,name='movies'),
    path('anime/',anime,name='anime'),
    path('show/',show,name='show'),
    path('originals/',originals,name='originals'),
    path('drama/',drama,name='drama'),
    path('documentaries/',documentaries,name='documentaries'),
    path('kid/',kid,name='kid'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# URLS
