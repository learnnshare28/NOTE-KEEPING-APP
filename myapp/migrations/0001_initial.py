# Generated by Django 3.1.1 on 2020-10-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_title', models.CharField(max_length=30)),
                ('note_description', models.CharField(max_length=350)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
