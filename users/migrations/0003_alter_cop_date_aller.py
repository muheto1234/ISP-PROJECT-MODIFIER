# Generated by Django 4.2.1 on 2023-12-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_cop_date_retour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cop',
            name='date_aller',
            field=models.DateField(blank=True),
        ),
    ]
