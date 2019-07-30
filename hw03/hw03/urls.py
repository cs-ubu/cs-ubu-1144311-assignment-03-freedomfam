from django.contrib import admin
from django.urls import path
from commath import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('Decimal32/',views.Decimal32),
    path('Decimal64/',views.Decimal64),
    path('solve/',views.datasolve),
]
