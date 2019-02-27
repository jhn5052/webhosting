"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import blog.views
import makepf.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('detail/<int:blog_id>', blog.views.detail, name="detail"),
    path('new/', blog.views.blogpost, name="new"),
    path('create/', blog.views.create, name="create"),
    path('newblog/', blog.views.blogpost, name="newblog"),
    path('ShowPortfolio/', makepf.views.ShowPortfolio, name="ShowPortfolio"),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
