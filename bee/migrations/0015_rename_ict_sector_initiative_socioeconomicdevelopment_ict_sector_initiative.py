# Generated by Django 5.0.6 on 2024-07-03 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0014_rename_amount_of_contribution_socioeconomicdevelopment_amount_of_contribution_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socioeconomicdevelopment',
            old_name='Ict_Sector_Initiative',
            new_name='ICT_Sector_Initiative',
        ),
    ]
