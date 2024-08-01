"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from main.views import get_page, get_add_car, detail_info, get_brand, search, registration, login_user, logaut_user, \
    kabinet, my_orders

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('main/', get_page, name='Home'),
    path('add_car/', get_add_car, name='add_car'),
    path('detail/<int:id>/', detail_info, name='detail_info'),
    path('brand/', get_brand, name='brand'),
    path('search/', search, name='search'),
    path('registration/', registration, name='registration'),
    path('login/', login_user, name='login'),
    path('logaut/', logaut_user, name='logaut'),
    path('kabinet/', kabinet, name='kabinet'),
    path('my_orders/', my_orders, name='my_orders'),
]
