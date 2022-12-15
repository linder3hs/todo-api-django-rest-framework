from rest_framework.routers import DefaultRouter
from .api import UserViewSet, UserViewGenericViewSet

from .routers import CustomRouter

user_router = DefaultRouter()
user_custom_router = CustomRouter()

user_router.register(r"users", UserViewSet, basename="users")
user_custom_router.register(r"custom/users", UserViewGenericViewSet, basename="users_custom")

urlpatterns = user_router.urls
urlpatterns += user_custom_router.urls
