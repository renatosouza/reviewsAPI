from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from reviews import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)