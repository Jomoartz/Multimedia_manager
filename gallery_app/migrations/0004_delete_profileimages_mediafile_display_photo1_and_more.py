# Generated by Django 5.0.4 on 2024-05-25 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0003_profileimages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileImages',
        ),
        migrations.AddField(
            model_name='mediafile',
            name='display_photo1',
            field=models.ImageField(blank='false', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='display_photo2',
            field=models.ImageField(blank='false', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='display_photo3',
            field=models.ImageField(blank='false', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='profile',
            field=models.ImageField(blank='True', upload_to='images/'),
        ),
    ]
