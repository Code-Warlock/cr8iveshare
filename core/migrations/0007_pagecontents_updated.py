# Generated by Django 4.0.4 on 2022-12-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_pagecontents_social_icon_5_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontents',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
