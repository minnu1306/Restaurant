from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Rest, Recipe, Ing
from django.http import Http404, HttpResponse,JsonResponse
from rest_framework import status


class Restaurants(APIView):

    def get(self, request):
        restaurants = Rest.objects.all()
        serializer = serializers.RestSe(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.RestSe(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):

    def get(self, request, restaurant_id):
        try:
            restaurant = Rest.objects.get(pk=restaurant_id)
        except Rest.DoesNotExist:
            raise Http404
        serializer = serializers.RestSe(restaurant)
        return Response(serializer.data)

    def delete(self, request, restaurant_id):
        try:
            restaurant = Rest.objects.get(pk=restaurant_id)
        except Rest.DoesNotExist:
            raise Http404
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Recipes(APIView):

    def get(self, request, restaurant_id):
        recipes = Recipe.objects.filter(restaurant__id=restaurant_id)
        serializer = serializers.RecipeSe(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, restaurant_id):
        try:
            Rest.objects.get(pk=restaurant_id)
        except Rest.DoesNotExist:
            raise Http404

        serializer = serializers.RecipeSe(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant_id=restaurant_id, ingredients=request.data.get("ingredients"))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetail(APIView):

    def get(self, request, restaurant_id, recipe_id):
        try:
            recipe = Recipe.objects.get(restaurant__id=restaurant_id, pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        serializer = serializers.RecipeSe(recipe)
        return Response(serializer.data)

    def delete(self, request, restaurant_id, recipe_id):
        try:
            recipe = Recipe.objects.get(restaurant__id=restaurant_id, pk=recipe_id)
        except Recipe.DoesNotExist:
            raise Http404
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
