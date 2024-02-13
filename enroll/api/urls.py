from django.contrib import admin
from django.urls import path,include
from enroll.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("todolist", views.todolistapi, basename="todolist")

urlpatterns = [
    
    path("", include(router.urls)),
]