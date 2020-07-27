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
from sikkimgov import  views as view
from rest_framework import routers

#from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
 
router = routers.DefaultRouter()
router.register('ben',view.benViewSet)
router.register('intermediator',view.intermediatorViewSet)

urlpatterns=router.urls



# router.register()

urlpatterns = [

    path('ben/',include(router.urls)),
    
 
    path('admin/', admin.site.urls),
    path('Intermediatorloginform/',include(router.urls)),
    path('scheme/',include('schemes.urls')),
    #path('router/',include(router.urls)),
    url(r'^api/', include(router.urls)),
    path('intermediatorlogin',views.intermediatorLogin.as_view()),
 
    path('verify',views.Verify)
]



from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
