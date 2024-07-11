# Generated by Django 5.0.6 on 2024-07-03 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0010_employmentequity_table_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employmentequity',
            old_name='black_youth_as_defined_by_the_national_youth_commission_act_of_1996',
            new_name='Black_Youth',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='description_of_disability',
            new_name='Description_of_disability',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='disabled',
            new_name='Disabled',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='foreign',
            new_name='Foreign',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='id_number',
            new_name='Id_number',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='job_title',
            new_name='Job_title',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='occupational_level',
            new_name='Occupational_level',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='pilot',
            new_name='Pilot',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='race',
            new_name='Race',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='surname',
            new_name='Surname',
        ),
        migrations.RenameField(
            model_name='employmentequity',
            old_name='technician',
            new_name='Technician',
        ),
    ]
