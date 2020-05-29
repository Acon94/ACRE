# Generated by Django 3.0.6 on 2020-05-25 21:15

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='listing',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=django_google_maps.fields.AddressField(max_length=200),
        ),
    ]
