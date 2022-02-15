from django.urls import path
from pwd_manager import views
from pwd_manager.views import hostinfo
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('hostinfo/', views.hosts_list),
    # path('hostinfo/<int:pk>/', views.hosts_detail),
    path('hostinfo/', hostinfo.hosts_list),
    path('hostinfo/<int:pk>/', hostinfo.hosts_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)