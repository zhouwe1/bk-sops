# Generated by Django 4.2 on 2025-03-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20230609_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='tenant_id',
            field=models.CharField(db_index=True, default='default', max_length=64, verbose_name='租户ID'),
        ),
        migrations.AddField(
            model_name='project',
            name='tenant_id',
            field=models.CharField(db_index=True, default='default', max_length=64, verbose_name='租户ID'),
        ),
    ]
