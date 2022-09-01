# Generated by Django 4.0.6 on 2022-07-08 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('persian', 'persian'), ('english', 'english'), ('arabic', 'arabic'), ('other', 'other')], default='persian', max_length=10),
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_on', models.DateTimeField(blank=True, null=True)),
                ('shelf_code', models.CharField(blank=True, max_length=50, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.category'),
        ),
    ]