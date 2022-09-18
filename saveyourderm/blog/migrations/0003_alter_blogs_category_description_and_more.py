# Generated by Django 4.1 on 2022-09-07 15:39

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blogs_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs_category",
            name="description",
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name="blogs_post", name="content", field=tinymce.models.HTMLField(),
        ),
    ]
