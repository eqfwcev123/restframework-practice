from django.urls import path, include

from members import apis

urlpatterns = [
    path('auth-token/', apis.AuthTokenAPIView.as_view())
]