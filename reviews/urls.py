from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from reviews import views


urlpatterns = [
    path('reviews/', views.ReviewList.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)