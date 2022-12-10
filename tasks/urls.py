from rest_framework.routers import DefaultRouter
from .views import TaskView

router = DefaultRouter()

router.register("todo", TaskView, basename="todo")
