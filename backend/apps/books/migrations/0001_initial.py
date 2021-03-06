# Generated by Django 3.2.5 on 2021-07-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('volume_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('authors', models.ManyToManyField(blank=True, null=True, to='authors.Author')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
