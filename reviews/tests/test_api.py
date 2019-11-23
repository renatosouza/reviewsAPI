from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework import status
from reviews.models import Review
from django.contrib.auth.models import User
from django.urls import reverse


class ReviewAPITests(APITestCase):
    """ Testing the API """
    
    def setUp(self):
        self.user = User.objects.create_user(username='tester', 
                                             password='1234')
        self.client = APIClient()
        self.review1_data = {
            'rating': 1,
            'title': 'dummy data 1',
            'summary': 'dummy data',
            'ip_address': '1.1.1.1',
            'company': 'dummy data',
            'reviewer': 'dummy data',
        }
        self.review2_data = {
            'rating': 2,
            'title': 'dummy data 2',
            'summary': 'dummy data',
            'ip_address': '1.1.1.1',
            'company': 'dummy data',
            'reviewer': 'dummy data',
        }
        self.review3_data = {
            'rating': 3,
            'title': 'dummy data 3',
            'summary': 'dummy data',
            'ip_address': '1.1.1.1',
            'company': 'dummy data',
            'reviewer': 'dummy data',
        }
        self.client.force_authenticate(user=self.user)
        self.client.post('/reviews/', self.review1_data, format='json')
        self.client.post('/reviews/', self.review2_data, format='json')
        self.client.post('/reviews/', self.review3_data, format='json')
    
    
    def test_get_token(self):
        url = reverse('api_token_auth')
        data = {'username': 'tester', 'password': '1234'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'token')
    
        
    def test_get_reviews(self):
        url = reverse('review_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
    
                    
    def test_create_review(self):
        url = reverse('review_list')
        data = {
            'rating': 1,
            'title': 'Awful book',
            'summary': 'Worst book I have ever read',
            'ip_address': '1.1.1.1',
            'company': 'Library Books',
            'reviewer': 'Book Reader'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 4)
    
    
    def test_create_review_mistakes(self):
        url = reverse('review_list')
        data = {
            'rating': 6,
            'title': 'Awful book',
            'summary': 'Worst book I have ever read',
            'ip_address': '1.1.1.1',
            'company': 'Library Books',
            'reviewer': 'Book Reader'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
        
    def test_get_review(self):
        url = '/reviews/1/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.review1_data['title'])
    
        
    def test_get_nonexistent_review(self):
        url = '/reviews/4/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)    
    
        
    def test_update_review(self):
        url = '/reviews/2/'
        data = {
            'rating': 2,
            'title': 'dummy data 2',
            'summary': 'dummy data',
            'ip_address': '2.2.2.2',
            'company': 'dummy data',
            'reviewer': 'dummy data',    
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.review2_data['title'])
        self.assertEqual(Review.objects.get(pk=2).ip_address, 
                         data['ip_address'])
    
        
    def test_delete_review(self):
        url = '/reviews/3/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 2)
    
        
    def test_get_users_admin(self):
        admin = User.objects.create_superuser(username='admin',
                                              email='admin@admin.com',
                                              password='0000')
        self.client.force_authenticate(user=admin)
        url = reverse('user_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)
    
    
    def test_get_user_admin(self):
        admin = User.objects.create_superuser(username='admin',
                                              email='admin@admin.com',
                                              password='0000')
        self.client.force_authenticate(user=admin)
        url = '/users/1/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get(pk=1).username, self.user.username)
        
    
    def test_access_forbidden(self):
        url = reverse('user_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)    
        
        
    def test_client_accessing_not_own_review(self):
        new_user = User.objects.create_user(username='new_tester',
                                            password='5678')
        self.client.force_authenticate(user=new_user)
        url = '/reviews/1/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)        