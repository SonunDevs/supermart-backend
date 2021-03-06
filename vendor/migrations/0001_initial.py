# Generated by Django 3.0.7 on 2020-07-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=350)),
                ('user_name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='upload logo')),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
