# Generated by Django 3.1.7 on 2022-04-01 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UniteEnseignement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Excel_file_upload', models.FileField(upload_to='excel')),
            ],
        ),
    ]
