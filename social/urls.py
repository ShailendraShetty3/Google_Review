from django.contrib import admin
from django.urls import path, include
from .views import ReviewsListCreateView, ReviewsDetail


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Social ",
        default_version='v1',
        description="Social",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="xyz@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/',  ReviewsListCreateView.as_view()),
    path('reviews/<int:id>/', ReviewsDetail.as_view(), name='user-detail'),
    # path('api-auth/', include('authentication.urls')),

    # path('swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
