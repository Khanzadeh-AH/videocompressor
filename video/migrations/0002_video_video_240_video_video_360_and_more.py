# Generated by Django 4.1 on 2022-08-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("video", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="video_240",
            field=models.FileField(null=True, upload_to="", verbose_name=""),
        ),
        migrations.AddField(
            model_name="video",
            name="video_360",
            field=models.FileField(null=True, upload_to="", verbose_name=""),
        ),
        migrations.AlterField(
            model_name="video",
            name="original_video",
            field=models.FileField(upload_to="media/", verbose_name=""),
        ),
    ]
