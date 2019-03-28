


from django.contrib import admin
from django.urls import path
from app7 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.indexPage),
    path('newPage/', views.details)
]
