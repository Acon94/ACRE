# Generated by Django 3.0.6 on 2020-05-26 13:58

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200525_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='amenitys',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Air Conditioned', 'Air Conditioned'), ('Board Aproval Required', 'Board Aproval Required'), ('Doorman', 'Doorman'), ('Dishwasher', 'Dishwasher'), ('Elevator', 'Elevator'), ('Furnished', 'Furnished'), ('Fireplace', 'Fireplace'), ('Loft', 'Loft'), ('Sublet', 'Sublet'), ('Storage', 'Storage'), ('Wash/Dryer in unit', 'Wash/Dryer in unit'), ('Public outdoor area', 'Public outdoor area'), ('Private outdoor area', 'Private outdoor area'), ('Pets allowed', 'Pets allowed'), ('Parking', 'Parking'), ('Smoke free', 'Smoke free'), ('Gym', 'Gym'), ('Has Parking', 'Has Parking')], max_length=214),
        ),
    ]
