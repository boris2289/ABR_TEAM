from django.urls import path
from .views import YouTubeLinkListCreate, YouTubeLinkDelete
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('youtube-links/', YouTubeLinkListCreate.as_view(), name='youtube-links-list-create'),
    path('youtube-links/<int:pk>/', YouTubeLinkDelete.as_view(), name='youtube-link-delete'),
]
