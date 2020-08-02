from django.db import models
import uuid

# Create your models here.
class Rest(models.Model):
    id=models.UUIDField(primary_key= True, default=uuid.uuid4, editable=False)
    name =models.CharField(max_length=20)
    direction= models.CharField(max_length = 20)
    phone= models.IntegerField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    type= models.CharField(max_length=20, choices=[('BREAKFAST','Breakfast'),('LUNCH', 'Lunch'), ('COFFEE', 'Coffee'),
                                     ('DINNER', 'Dinner')])
    thumbnail = models.ImageField(upload_to="recipe_thumbnails", default="recipe_thumbnails/default.png")
    restaurant = models.ForeignKey(Rest, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ing(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    recipe = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name