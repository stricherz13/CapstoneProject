# Generated by Django 4.1.7 on 2023-04-12 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0003_alter_stlouiscitylandtax_sale"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stlouiscitylandtax",
            name="neighborho",
            field=models.CharField(
                blank=True, db_index=True, max_length=254, null=True
            ),
        ),
    ]
