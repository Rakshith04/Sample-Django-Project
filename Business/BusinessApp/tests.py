import pytest
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Business  
from .views import BusinessListView 
from .forms import BusinessModelForm  

class TestHomePageView(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create some test data
        for i in range(10):
            Business.objects.create(
                organisation_name=f'Business {i}',
                address = f'address {i}',
                owner_info = self.user,
                employee_size = i

            )

    def test_home_page_view(self):
        self.client.force_login(self.user)

        url = reverse('home')

        # Test for a successful response
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test for the correct template used
        self.assertTemplateUsed(response, 'business_detail_form.html')

        # Test for the presence of expected context in the response
        self.assertIn('business', response.context)
        self.assertTrue(response.context['business'])

        # Test the pagination
        self.assertIn('is_paginated', response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertIn('object_list', response.context)
        self.assertEqual(len(response.context['object_list']), 5)

class TestBusinessListView(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create some test data
        self.business1 = Business.objects.create(
            organisation_name='Test Organization 1',
                            address = f'address 1',
                owner_info = self.user,
                employee_size = 1
        )
        self.business2 = Business.objects.create(
            organisation_name='Another Test Organization 2',
                  address = f'address 2',
                owner_info = self.user,
                employee_size = 2
        )

    def test_business_list_view_with_search_query(self):
        request = RequestFactory().get(reverse('search') + '?search=test')
        request.user = self.user
        response = BusinessListView.as_view()(request)

        # Test for a successful response
        self.assertEqual(response.status_code, 200)

    def test_business_list_view_without_search_query(self):
        request = RequestFactory().get(reverse('search'))
        request.user = self.user
        response = BusinessListView.as_view()(request)

        # Test for a successful response
        self.assertEqual(response.status_code, 200)

class TestBusinessCreateView(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Create some test data
        for i in range(1, 10):
            Business.objects.create(
                organisation_name=f'Business {i}',
                address = f'address {i}',
                owner_info = self.user,
                employee_size = i
            )

    def test_business_create_view(self):
        url = reverse('create')
        self.client.force_login(self.user)
        # Test for a successful response for a GET request
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test for the correct template used
        assert 'business_create_form.html' in [t.name for t in response.templates]

        # Test for the use of the correct form class
        assert isinstance(response.context['form'], BusinessModelForm)

        # Test for a successful creation of a new Business object with a POST request
        response = self.client.post(url, data={'organisation_name': 'Test Organization', 
                                               'address':'Test Address', 
                                               'owner_info': self.user, 
                                               'employee_size': 20})
        assert response.status_code == 200 
       
class TestBusinessUpdateView(TestCase):

    def test_business_update_view(self,):
        self.user = User.objects.create_user(username='testuser', password='12345')
        business = Business.objects.create(
                organisation_name=f'Business',
                address = f'address',
                owner_info = self.user,
                employee_size = 1)
        url = reverse('update', kwargs={'pk': business.pk})
        self.client.force_login(self.user)
        # Test for a successful response for a GET request
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test for the correct template used
        assert 'business_edit_form.html' in [t.name for t in response.templates]

        # Test for the use of the correct form class
        assert isinstance(response.context['form'], BusinessModelForm)

@pytest.mark.django_db
def test_business_delete_view(client):
    # Create a Business object to delete
    user = User.objects.create_user(username='testuser', password='12345')
    business = Business.objects.create(organisation_name="Test Organization", 
                                               address='Test Address', 
                                               owner_info= user, 
                                               employee_size =  20)

    url = reverse('delete', kwargs={'pk': business.pk})

    # Test for a successful deletion of the Business object with a POST request
    response = client.post(url)
    assert response.status_code == 302