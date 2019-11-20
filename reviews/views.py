from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import generics


# Create your views here.
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer