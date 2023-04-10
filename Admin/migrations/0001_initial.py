# Generated by Django 3.2.12 on 2023-04-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('create', models.DateField()),
                ('proof', models.IntegerField(max_length=100)),
                ('detail', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Liquor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('proof', models.IntegerField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('detail', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('whisky', '위스키')], max_length=20)),
                ('country', models.CharField(choices=[('Y', '있음'), ('N', '없음')], max_length=20)),
                ('amount', models.IntegerField()),
                ('case', models.CharField(choices=[('Y', '있음'), ('N', '없음')], max_length=1)),
                ('price', models.IntegerField()),
                ('reviews', models.IntegerField()),
            ],
        ),
    ]