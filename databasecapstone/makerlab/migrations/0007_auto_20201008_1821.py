# Generated by Django 3.1.1 on 2020-10-08 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makerlab', '0006_auto_20201007_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='inusemachine',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makerlab.item', to_field='item_name'),
        ),

    ]