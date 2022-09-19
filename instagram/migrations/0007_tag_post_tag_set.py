# Generated by Django 4.1.1 on 2022-09-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instagram", "0006_alter_comment_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="tag_set",
            field=models.ManyToManyField(blank=True, to="instagram.tag"),
        ),
    ]
