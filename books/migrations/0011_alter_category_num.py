# Generated by Django 4.0.6 on 2022-07-29 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_category_num_alter_category_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='num',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
    ]