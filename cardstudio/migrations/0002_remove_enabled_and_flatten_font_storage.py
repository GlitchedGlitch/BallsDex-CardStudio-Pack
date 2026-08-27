from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardstudio", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cardconfig",
            name="enabled",
        ),
        migrations.AlterField(
            model_name="cardconfig",
            name="title_font",
            field=models.FileField(blank=True, help_text="Title font (.ttf/.otf).", null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="cardconfig",
            name="capacity_name_font",
            field=models.FileField(
                blank=True, help_text="Ability name font (.ttf/.otf).", null=True, upload_to=""
            ),
        ),
        migrations.AlterField(
            model_name="cardconfig",
            name="capacity_description_font",
            field=models.FileField(
                blank=True, help_text="Ability description font (.ttf/.otf).", null=True, upload_to=""
            ),
        ),
        migrations.AlterField(
            model_name="cardconfig",
            name="stats_font",
            field=models.FileField(blank=True, help_text="Health/attack font.", null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="cardconfig",
            name="credits_font",
            field=models.FileField(blank=True, help_text="Credits font.", null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="cardconfig",
            name="rarity_font",
            field=models.FileField(blank=True, help_text="Rarity font.", null=True, upload_to=""),
        ),
    ]
