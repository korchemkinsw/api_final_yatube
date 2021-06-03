from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, 'post')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    'comment')
router_v1.register('group', GroupViewSet, 'group')
router_v1.register('follow', FollowViewSet, 'follow')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router_v1.urls)),
]
