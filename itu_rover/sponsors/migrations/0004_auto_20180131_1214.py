# Generated by Django 2.0.1 on 2018-01-31 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_sponsorshiptype_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsorshiptype',
            options={'ordering': ('priority',)},
        ),
    ]
