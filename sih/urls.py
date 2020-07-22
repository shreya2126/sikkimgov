"""sih URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from sikkimgov import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from sikkimgov import  views as as_view
from rest_framework import routers
#from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()
router.register('beneficiaries', views.beneficiaries)
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    
    url(r'^beneficiaries/',views.beneficiaries.as_view(),name="beneficiaries"),
    path('classify/',views.call_model.as_view(),name="model"),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^intermediatorloginform/$',views.intermediatorloginform.as_view(), name="Intermediatorloginform"),
    path('scheme/',include('schemes.urls')),
    path('user/',include('sikkimgov.urls')),
    path('login',views.UserLogin.as_view()),
    path('intermediatorlogin',views.intermediatorLogin.as_view())
]



from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
