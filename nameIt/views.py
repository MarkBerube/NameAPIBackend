from django.shortcuts import render
from nameIt.models import Title, First, Last
from nameIt.serializers import TitleSerializer, FirstSerializer, LastSerializer, TitleURLSerializer, FirstURLSerializer, LastURLSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from random import randint

class RootList(APIView):
    def get(self, request, format=None):
        return Response({
        	'title': reverse('titleList', request=request, format=format),
        	'first': reverse('firstList', request=request, format=format),
        	'last': reverse('lastList', request=request, format=format),
        	'random': reverse('random', request=request, format=format),
        })

class TitleList(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleURLSerializer

class TitleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleURLSerializer

class FirstList(generics.ListCreateAPIView):
    queryset = First.objects.all()
    serializer_class = FirstURLSerializer

class FirstDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = First.objects.all()
    serializer_class = FirstURLSerializer

class LastList(generics.ListCreateAPIView):
    queryset = Last.objects.all()
    serializer_class = LastURLSerializer

class LastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Last.objects.all()
    serializer_class = LastURLSerializer

class RandomDetail(APIView):
    def get(self, request, format=None):
    	firstSerializer = FirstSerializer(First.objects.all().order_by('?')[:1].get())
        lastSerializer = LastSerializer(Last.objects.all().order_by('?')[:1].get())

        if randint(1,10) >= 7:
            titleSerializer = TitleSerializer(Title.objects.all().order_by('?')[:1].get())
            responseData = {
                'title': titleSerializer.data,
                'first': firstSerializer.data,
                'last': lastSerializer.data,
            }
        else:
            responseData = {
                'first': firstSerializer.data,
                'last': lastSerializer.data,
            }
        return Response(responseData)
