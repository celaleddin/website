# Generated by Django 2.0.1 on 2020-02-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0013_auto_20190302_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorshiptype',
            name='eng_name',
            field=models.CharField(default='', max_length=30, verbose_name='eng type name'),
            preserve_default=False,
        ),
    ]
