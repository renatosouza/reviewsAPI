from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Review
from .serializers import ReviewSerializer, UserSerializer
from .permissions import IsOwner
from rest_framework import generics, permissions


# Create your views here.
class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return Review.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        # maybe permission IsOwner unnecessary because of filter
        return Review.objects.filter(owner=self.request.user)
    
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer