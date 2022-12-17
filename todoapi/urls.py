from django.contrib import admin
from django.urls import path, include, re_path
# from tasks.urls import router
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Todo Api",
        default_version="v1",
        description="API de lista de tareas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="linderhassinger00@gmail.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=[AllowAny]
)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r"api/", include("tasks_viewset.urls")),
    # path("api/v1/", include(router.urls)),
    path(r"api/v1/", include("tasks.urls")),
    path(r"api/v1/", include("users.urls")),
    path(r"api-auth/", include("authapp.urls")),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
