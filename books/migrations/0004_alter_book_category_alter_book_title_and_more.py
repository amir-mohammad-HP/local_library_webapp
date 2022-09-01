# Generated by Django 4.0.6 on 2022-07-08 06:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, default='No Category', null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=250, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'باید حداقل ۲ کاراکتر باشد')]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'باید حداقل ۲ کاراکتر باشد')]),
        ),
    ]