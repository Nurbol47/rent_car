from django.shortcuts import render
from rest_framework import generics
from .serializers import *


class PricingPlanView(generics.ListAPIView):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer    




