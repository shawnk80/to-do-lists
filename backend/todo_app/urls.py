## wines/urls.py
from django.urls import path, include
from .views import ListViewSet, TaskViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSet, basename='list')
router.register(r'tasks', TaskViewSet, basename='task')
urlpatterns = router.urls
