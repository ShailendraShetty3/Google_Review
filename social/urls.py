from django.contrib import admin
from django.urls import path, include
from .views import PostListCreateView, PostDetail, Post_MetaListCreateView, Post_MetaDetail, CommentListCreateView, CommentDetail
from .views import UserListCreateView, UsertDetail

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
    path('post/',  PostListCreateView.as_view()),
    path('post/<int:id>/', PostDetail.as_view(), name='user-detail'),
    path('post_meta/',  Post_MetaListCreateView.as_view()),
    path('post_meta/<int:id>/', Post_MetaDetail.as_view()),
    path('comment/',  CommentListCreateView.as_view()),
    path('comment/<int:id>/', CommentDetail.as_view() ),
    path('users/',  UserListCreateView.as_view()),
    path('users/<int:id>/', UsertDetail.as_view() ),



    path('swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
