from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework.authtoken import views

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>[\d]+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]
