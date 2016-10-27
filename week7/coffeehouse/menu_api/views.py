from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from menu_api.models import Special, Ingredient
from menu_api.serializers import SpecialSerializer, IngredientSerializer
from menu_api.permissions import IsCreatedByOrReadOnly

class SpecialListCreateAPIView(ListCreateAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer

    def perform_create(self, *args, **kwargs):
        return super().perform_create(serializer)

class SpecialDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
    permission_classes = (IsCreatedByOrReadOnly, )

class IngredientListAPIView(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetailAPIView(RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
