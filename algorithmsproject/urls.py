from django.contrib import admin
from django.urls import path
import algorithmsprojectapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', algorithmsprojectapp.views.home, name='home'),
]
