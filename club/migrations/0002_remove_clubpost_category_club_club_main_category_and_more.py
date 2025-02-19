# Generated by Django 5.0.2 on 2024-05-22 10:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
        ('teenplay_server', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubpost',
            name='category',
        ),
        migrations.AddField(
            model_name='club',
            name='club_main_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='teenplay_server.category'),
        ),
        migrations.AddField(
            model_name='club',
            name='club_region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='teenplay_server.region'),
        ),
        migrations.CreateModel(
            name='ClubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teenplay_server.category')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='club.club')),
            ],
            options={
                'db_table': 'tbl_club_category',
            },
        ),
    ]
