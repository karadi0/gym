# Generated by Django 2.2.6 on 2020-06-08 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Status'),
        ),
    ]
