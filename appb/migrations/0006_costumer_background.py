# Generated by Django 3.0.8 on 2020-12-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appb', '0005_auto_20201216_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='background',
            field=models.ImageField(default='media/image/IMG_20191007_233026_695.jpg', height_field='400', upload_to='media/bgimg'),
        ),
    ]
