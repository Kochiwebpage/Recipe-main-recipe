# Generated by Django 5.0 on 2023-12-11 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recipe_app', '0002_recipes_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='recipes',
            name='food_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Recipe_app.foodtype'),
        ),
    ]
