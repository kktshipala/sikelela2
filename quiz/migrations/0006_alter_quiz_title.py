# Generated by Django 3.2.23 on 2024-01-25 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_quiz_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(blank=True, max_length=60, verbose_name='Title'),
        ),
    ]
