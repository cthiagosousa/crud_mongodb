from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AccountViewSet

urlpatterns = [
    path('account/', AccountViewSet.as_view({ 'get': 'list', 'post': 'create' })),
    path('account/<str:pk>', AccountViewSet.as_view({ 'get': 'account_details', 'put': 'update', 'delete': 'destroy' })),
]

urlpatterns = format_suffix_patterns(urlpatterns)
