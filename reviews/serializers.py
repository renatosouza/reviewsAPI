from rest_framework import serializers
from .models import Review
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    submitted_at = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Review
        fields = ['id', 'rating', 'title', 'summary', 
                  'ip_address', 'company', 'reviewer', 
                  'submitted_at', 'owner']
        

class UserSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, 
                                                 queryset=Review.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'reviews']