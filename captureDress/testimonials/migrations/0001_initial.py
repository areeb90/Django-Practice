# Generated by Django 4.2 on 2023-04-23 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('testimonial', models.TextField()),
                ('rating', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='testimonials/')),
            ],
        ),
    ]
