# Generated by Django 2.2.16 on 2020-11-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
