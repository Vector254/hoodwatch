# Generated by Django 3.1.2 on 2020-10-31 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoodwatch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='occupants', to='hoodwatch.neighbourhood'),
        ),
    ]
