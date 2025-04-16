from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/transcriptions/', include('transcriptions.urls')),
    path(
        'api/auth/token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/auth/token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
