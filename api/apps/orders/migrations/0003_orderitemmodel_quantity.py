# Generated by Django 2.2.6 on 2019-10-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_ordermodel_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemmodel',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
