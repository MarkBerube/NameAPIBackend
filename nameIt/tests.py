from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from nameIt.models import First, Last, Title, FONT_CHOICES
from nameIt.serializers import TitleSerializer, FirstSerializer, LastSerializer, TitleURLSerializer, FirstURLSerializer, LastURLSerializer
from rest_framework.parsers import JSONParser

class NameTests(APITestCase):
    def test_create_firstname(self):
        """
        testing POST first name
        """
        url = reverse('firstList')
        data = {'value': 'Foobar', 'font': 'comic'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(First.objects.count(), 1)
        self.assertEqual(First.objects.get().value, 'Foobar')
    def test_create_lastname(self):
        """
        testing POST last name
        """
        url = reverse('lastList')
        data = {'value': 'Foobar', 'font': 'comic'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Last.objects.count(), 1)
        self.assertEqual(Last.objects.get().value, 'Foobar')
    def test_create_title(self):
        """
        testing POST title name
        """
        url = reverse('titleList')
        data = {'value': 'Foobar', 'font': 'comic'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Title.objects.count(), 1)
        self.assertEqual(Title.objects.get().value, 'Foobar')
    def test_get_firstname(self):
        """
        testing GET first name
        """
        url = reverse('firstList')
        data = {'value': 'Foobar', 'font': 'comic'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(First.objects.count(), 1)
        self.assertEqual(First.objects.get().value, 'Foobar')
        url += '1/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = FirstSerializer(data=response.data)
        self.assertEqual(serializer.is_valid(), True)
    def test_get_lastname(self):
        """
        testing GET last name
        """
        url = reverse('lastList')
        data = {'value': 'Foobar', 'font': 'comic'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Last.objects.count(), 1)
        self.assertEqual(Last.objects.get().value, 'Foobar')
        url += '1/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = LastSerializer(data=response.data)
        self.assertEqual(serializer.is_valid(), True)
    def test_get_title(self):
        """
        testing GET title name
        """
        url = reverse('titleList')
        data = {'value': 'Foobar', 'font': 'comic'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Title.objects.count(), 1)
        self.assertEqual(Title.objects.get().value, 'Foobar')
        url += '1/'
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = TitleSerializer(data=response.data)
        self.assertEqual(serializer.is_valid(), True)