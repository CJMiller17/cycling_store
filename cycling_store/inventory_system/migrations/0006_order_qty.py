# Generated by Django 5.0.6 on 2024-05-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_system', '0005_rename_transport_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='qty',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
