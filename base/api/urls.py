
from django.urls import path
from .auth import AuthService
# from .auth.AuthService import MyTokenObtainPairView
from .projects import ProjectService

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('index/', AuthService.get_welcome_page),
    path('index/project', ProjectService.list_projects),
    path('profile/', AuthService.get_profile),
    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
