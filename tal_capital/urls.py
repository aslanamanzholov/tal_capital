from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.reverse import reverse_lazy
from rest_framework.routers import DefaultRouter

from tal_capital.core.views import PostViewSet
from tal_capital.users.views import CapitalObtainAuthToken, ChangePassword, UserCreateViewSet, UserViewSet

router = DefaultRouter()
router.register(r'user', UserCreateViewSet, base_name='user_create')
router.register(r'users', UserViewSet, base_name='user_list')
router.register(r'post', PostViewSet, base_name='post_list')

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/v1/', include(router.urls)),
    path(r'api-token-auth/', CapitalObtainAuthToken.as_view()),
    path(r'change-password/', ChangePassword.as_view()),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += [
    path(r'api/docs', include_docs_urls(title='Capital API', permission_classes=[permissions.AllowAny])),
]