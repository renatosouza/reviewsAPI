import unittest
from django.test import TestCase
from .models import Review
from .serializers import ReviewSerializer
from django.contrib.auth.models import User


# Create your tests here.
class ReviewTest(TestCase):
    """ Testing model Review """
    
    def setUp(self):
        self.user = User.objects.create_user(username="tester", 
                                             password="1234")
        self.review1_attributes = {
            'rating': 1,
            'title': 'Awful book',
            'summary': 'Worst book I have ever read',
            'ip_address': '1.1.1.1',
            'company': 'Library Books',
            'reviewer': 'Book Reader',
            'owner': self.user
        }
        self.review2_attributes = {
            'rating': 3,
            'title': 'Regular sushi',
            'summary': 'Not the worst, but it could be better',
            'ip_address': '2.2.2.2',
            'company': 'Sushi Place',
            'reviewer': 'Sushi Eater',
            'owner': self.user
        }
        self.review1 = Review.objects.create(**self.review1_attributes)
        self.review2 = Review.objects.create(**self.review2_attributes)
        
    def test_rating_content(self):
        self.assertEqual(self.review1_attributes['rating'], 
                         self.review1.rating)
        
    def test_title_content(self):
        self.assertEqual(self.review1_attributes['title'], 
                         self.review1.title)
    
    def test_summary_content(self):
        self.assertEqual(self.review1_attributes['summary'], 
                         self.review1.summary)
        
    def test_ip_address_content(self):
        self.assertEqual(self.review1_attributes['ip_address'], 
                         self.review1.ip_address)
    
    def test_company_content(self):
        self.assertEqual(self.review1_attributes['company'], 
                         self.review1.company)
        
    def test_reviewer_content(self):
        self.assertEqual(self.review1_attributes['reviewer'], 
                         self.review1.reviewer)
        
    def test_owner_content(self):
        self.assertEqual(self.review1_attributes['owner'], 
                         self.review1.owner)    
        
    def test_order_of_reviews(self):
        #the first created is the last in the list
        last_review = Review.objects.last()
        self.assertEqual(self.review1, last_review)
        
        
class ReviewSerializerTeste(TestCase):
    """ Testing ReviewSerializer """
    
    def setUp(self):
        self.user = User.objects.create_user(username="tester", 
                                                 password="1234")
        
        self.review_attributes = {
            'rating': 5,
            'title': 'Awesome pizza',
            'summary': 'Best pizza I ever had',
            'ip_address': '1.3.5.7',
            'company': 'PizzaPlace',
            'reviewer': 'Pizza Eater',
            'owner': self.user
        }
        #valid serializer data to test edge cases
        self.serializer_data = {
            'rating': 5,
            'title': 'Awesome pizza',
            'summary': 'Best pizza I ever had',
            'ip_address': '1.3.5.7',
            'company': 'PizzaPlace',
            'reviewer': 'Pizza Eater',
            'owner': self.user
        }
        self.review = Review.objects.create(**self.review_attributes)
        self.review_serializer = ReviewSerializer(instance=self.review)
        
    def test_contain_expected_fields(self):
        data = self.review_serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'rating', 'title', 
                                                'summary', 'ip_address', 
                                                'company', 'reviewer', 
                                                'owner', 'submitted_at']))
        
    def test_rating_field_content(self):
        data = self.review_serializer.data
        self.assertEqual(data['rating'], self.review_attributes['rating'])
        
    def test_title_field_content(self):
        data = self.review_serializer.data
        self.assertEqual(data['title'], self.review_attributes['title'])
        
    def test_summary_field_content(self):
        data = self.review_serializer.data    
        self.assertEqual(data['summary'], self.review_attributes['summary'])
        
    def test_ip_address_field_content(self):
        data = self.review_serializer.data    
        self.assertEqual(data['ip_address'], self.review_attributes['ip_address'])
        
    def test_company_field_content(self):
        data = self.review_serializer.data    
        self.assertEqual(data['company'], self.review_attributes['company'])
        
    def test_reviewer_field_content(self):
        data = self.review_serializer.data
        self.assertEqual(data['reviewer'], self.review_attributes['reviewer'])
        
    def test_owner_field_content(self):
        data = self.review_serializer.data    
        self.assertEqual(data['owner'], self.review_attributes['owner'].username)
        
    def test_rating_out_choices(self):
        self.serializer_data['rating'] = 6
        serializer = ReviewSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['rating']))