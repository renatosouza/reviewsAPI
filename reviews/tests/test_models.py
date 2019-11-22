from django.test import TestCase
from reviews.models import Review
from django.contrib.auth.models import User


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