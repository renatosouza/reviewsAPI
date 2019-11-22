from django.test import TestCase
from .models import Review
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