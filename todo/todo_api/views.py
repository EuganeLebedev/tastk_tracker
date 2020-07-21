from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework import views


class IndexView(views.APIView):

    def get(self, request):

        return Responce([1])

