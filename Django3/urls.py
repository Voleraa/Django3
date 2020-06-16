"""Django3 URL Configuration

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
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls import url
from Django3 import settings
from Django3.settings import MEDIA_ROOT
from django.views.generic.base import RedirectView
from web import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('voler.urls')),
    path('blog/', include('voler.urls')),
    path('web/', include('web.urls')),
    path('accounts/', include('user.urls')),
    path('student/<int:id>/', views.student),
    path('admin/', admin.site.urls),
    path('maeditor/', include('mdeditor.urls')),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    # favicon.cio
    url('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
    # re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATICFILES_DIRS}),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
