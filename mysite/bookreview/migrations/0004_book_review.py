# Generated by Django 3.0.4 on 2020-03-30 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0003_auto_20200330_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
