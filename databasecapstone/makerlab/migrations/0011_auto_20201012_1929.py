# Generated by Django 3.1.1 on 2020-10-13 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makerlab', '0010_remove_vendor_warranty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inusemachine',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makerlab.item'),
        ),
    ]
