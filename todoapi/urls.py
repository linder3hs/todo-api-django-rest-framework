from django.contrib import admin
from django.urls import path, include
# from tasks.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("tasks_viewset.urls")),
    # path("api/v1/", include(router.urls)),
    path("api/v1/", include("tasks.urls")),
    path("api-auth/", include("authapp.urls"))
]
