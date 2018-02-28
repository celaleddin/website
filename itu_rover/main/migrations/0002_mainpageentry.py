# Generated by Django 2.0.1 on 2018-02-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
                'ordering': ('order',),
            },
        ),
    ]