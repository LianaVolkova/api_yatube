from rest_framework.routers import SimpleRouter

from django.urls import include, path

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
