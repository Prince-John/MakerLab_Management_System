# Generated by Django 3.1.1 on 2020-10-05 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makerlab', '0004_auto_20201005_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='user_id',
            field=models.CharField(max_length=250),
        ),
    ]
