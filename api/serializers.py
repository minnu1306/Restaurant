from rest_framework import serializers
from .models import Rest, Recipe, Ing
import os
import base64
from django.conf import settings

class RestSe(serializers.ModelSerializer):
    class Meta:
        model= Rest
        fields='__all__'

class RecipeSe(serializers.ModelSerializer):
    ingredients= serializers.SerializerMethodField('get_ing')
    thumbnail= serializers.SerializerMethodField('get_thum')
    def get_thum(self,recipe):
        with open(os.path.join(settings.MEDIA_ROOT, recipe.thumbnail.name), "rb") as image_file:
            return base64.b64encode(image_file.read())

    def get_ing(self,recipe):
        try:
            ing=Ing.objects.filter(id =recipe.id)
            serializer=IngSe(ing, many=True)
            return serializer.data
        except Ing.DoesNotExist:
            return none

    def create(self, validated_data):
        ingredients_data = validated_data.pop("ingredients")

        restaurant = Rest.objects.get(pk=validated_data["restaurant_id"])
        validated_data["restaurant"] = restaurant
        recipe = Recipe.objects.create(**validated_data)

        # Assign ingredients if they are present in the body
        if ingredients_data:
            for ingredient_dict in ingredients_data:
                ingredient = Ing(name=ingredient_dict["name"])
                ingredient.save()
                ingredient.recipe.add(recipe)
        return recipe

    class Meta:
        model=Recipe
        fields=['id','name','type','thumbnail','ingredients']

class IngSe(serializers.ModelSerializer):
    class Meta:
        model= Ing
        fields='__all__'