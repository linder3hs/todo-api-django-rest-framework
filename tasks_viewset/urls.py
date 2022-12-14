from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskReadOnlyViewSet

tasks_router = DefaultRouter()

tasks_router.register(r"v2/todo", TaskViewSet, basename="todo_model_viewset")
tasks_router.register(r"v3/todo", TaskReadOnlyViewSet, basename="todo_read_only_model_viewset")

urlpatterns = tasks_router.urls
