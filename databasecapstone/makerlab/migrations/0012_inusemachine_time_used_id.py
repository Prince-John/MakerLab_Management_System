# Generated by Django 3.1.1 on 2020-10-13 01:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makerlab', '0011_auto_20201012_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='inusemachine',
            name='time_used_id',
            field=models.ForeignKey(default= -1, on_delete=django.db.models.deletion.CASCADE, to='makerlab.entryexit'),
            preserve_default=False,
        ),
    ]
