# Generated by Django 4.0.2 on 2022-02-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressbook',
            name='address',
            field=models.CharField(default='no address recorded', max_length=250),
        ),
    ]
