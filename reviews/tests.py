import unittest
from django.test import TestCase
from .models import Review
from .serializers import ReviewSerializer, UserSerializer
from django.contrib.auth.models import User


# Create your tests here.
class ReviewTest(TestCase):
    """ Testing model Review """
    
    def setUp(self):
        user = User.objects.create_user(username="testy", password="1234")
        Review.objects.create(rating=1, 
                              title="Testing1", 
                              summary="this is a test", 
                              ip_address="1.1.1.1", 
                              company="Tester", 
                              reviewer="Testy Tester",
                              owner=user)
        Review.objects.create(rating=2, 
                              title="Testing2", 
                              summary="this is a new test", 
                              ip_address="1.1.1.1", 
                              company="Tester", 
                              reviewer="Testy Tester",
                              owner=user)
        
        
    def test_fields(self):
        review_test = Review.objects.get(title="Testing1")
        self.assertEqual(review_test.company, "Tester")
        self.assertEqual(review_test.summary, "this is a test")
        self.assertEqual(review_test.reviewer, "Testy Tester")
        self.assertEqual(review_test.ip_address, "1.1.1.1")
        
    def test_order_of_reviews(self):
        #the first created is the last in the list
        review_test = Review.objects.get(title="Testing1")
        last_review = Review.objects.last()
        self.assertEqual(review_test, last_review)
        
        
class ReviewSerializerTeste(TestCase):
    """ Testing ReviewSerializer """
    
    def setUp(self):
        try:
            self.user = User.objects.get(username="tester")
        except:
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