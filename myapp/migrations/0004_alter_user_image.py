# Generated by Django 4.1.6 on 2023-02-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile.pics'),
        ),
    ]
