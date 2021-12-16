# Generated by Django 2.2.6 on 2020-06-11 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_auto_20200611_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='time_table',
        ),
        migrations.AddField(
            model_name='attendance',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gym.Batch'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='dot',
            field=models.DateField(null=True),
        ),
    ]
