# Generated by Django 3.2.21 on 2023-11-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20231128_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-11-28 17:00:2'),
            preserve_default=False,
        ),
    ]
