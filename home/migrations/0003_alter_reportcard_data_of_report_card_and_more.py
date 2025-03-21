# Generated by Django 5.1.5 on 2025-03-09 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_subjectmarks_student_reportcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='data_of_report_card',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('rank', 'data_of_report_card')},
        ),
    ]
