# Generated by Django 5.0.2 on 2024-05-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_member_member_keyword1_member_member_keyword2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_recommended_club_model',
            field=models.TextField(null=True),
        ),
    ]
