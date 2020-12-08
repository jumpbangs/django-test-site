# Generated by Django 3.1.4 on 2020-12-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('permalink', models.CharField(default='#', max_length=12, unique=True)),
                ('update_date', models.DateTimeField(verbose_name='Last updated')),
                ('body_text', models.TextField(blank=True, verbose_name='Page Content')),
            ],
        ),
    ]
