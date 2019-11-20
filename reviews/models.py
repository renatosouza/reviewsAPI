from django.db import models


RATING_CHOICES = [
    (1, 'not satisfied'),
    (2, 'partly satisfied'),
    (3, 'satisfied'),
    (4, 'more than satisfied'),
    (5, 'very satisfied')
]


# Create your models here.
class Review(models.Model):
    rating = models.IntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=64)
    summary = models.TextField()
    ip_address = models.CharField(max_length=15)
    submitted_at = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=50)
    reviewer = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', 
                              related_name='snippets', 
                              on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-submitted_at']