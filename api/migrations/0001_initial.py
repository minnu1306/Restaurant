# Generated by Django 3.0.8 on 2020-07-14 19:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('direction', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('COFFEE', 'Coffee'), ('DINNER', 'Dinner')], max_length=20)),
                ('thumbnail', models.ImageField(default='recipe_thumbnails/default.png', upload_to='recipe_thumbnails')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Rest')),
            ],
        ),
        migrations.CreateModel(
            name='Ing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('recipe', models.ManyToManyField(to='api.Recipe')),
            ],
        ),
    ]
