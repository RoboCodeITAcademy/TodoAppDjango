# Generated by Django 3.2.4 on 2021-06-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('text', models.CharField(blank=True, max_length=800, verbose_name='Text')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
                ('done', models.BooleanField(default=False, verbose_name='Done ?')),
                ('priority', models.CharField(blank=True, choices=[('red', 'RED'), ('green', 'GREEN'), ('yellow', 'YELLOW')], max_length=50, verbose_name='Priority')),
            ],
        ),
    ]
