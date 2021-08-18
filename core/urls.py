from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AccountViewSet

urlpatterns = [
    path('account/', AccountViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'put': 'update',
        'delete': 'destroy',
    })),
]

urlpatterns = format_suffix_patterns(urlpatterns)
