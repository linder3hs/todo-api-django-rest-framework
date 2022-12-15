from django.contrib import admin
from django.urls import path, include
# from tasks.urls import router

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r"api/", include("tasks_viewset.urls")),
    # path("api/v1/", include(router.urls)),
    path(r"api/v1/", include("tasks.urls")),
    path(r"api/v1/", include("users.urls")),
    path(r"api-auth/", include("authapp.urls"))
]
