from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    submitted_at = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'rating', 'title', 'summary', 
                  'ip_address', 'company', 'reviewer', 'submitted_at']