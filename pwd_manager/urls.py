from django.urls import path
from pwd_manager import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('hostinfo/', views.hosts_list),
    path('hostinfo/<int:pk>/', views.hosts_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)