# Generated by Django 2.2.6 on 2020-06-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_auto_20200612_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=30, null=True)),
                ('timing', models.CharField(max_length=100, null=True)),
                ('what_to_eat', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
