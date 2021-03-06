# Generated by Django 4.0.5 on 2022-06-25 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.TextField(blank=True, max_length=209, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(blank=True, max_length=59, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
