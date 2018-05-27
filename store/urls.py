"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework import routers
from rest_framework.authtoken import views
from stoke.viewsets import ItemsViewSet
from sale.viewsets import CartViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemsViewSet, base_name='items')

urlpatterns = [
    path('', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('api/cart/', CartViewSet.as_view({'get': 'get_cart'})),
    path('api/add/item/', CartViewSet.as_view({'post': 'add_item'})),
    path('api/remove/item/', CartViewSet.as_view({'post': 'remove_item'})),
    path('api/order/', OrderViewSet.as_view({'get': 'get_order'})),
    path('api/create/order/', OrderViewSet.as_view({'post': 'create_order'})),
]
