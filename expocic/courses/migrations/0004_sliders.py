# Generated by Django 4.2.6 on 2024-02-26 11:16

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("courses", "0003_cursopage_delete_curso"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sliders",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sort_order", models.IntegerField(blank=True, editable=False, null=True)),
                ("title_slider", models.CharField(max_length=100)),
                ("paragraph_slider", wagtail.fields.RichTextField(default="Insira aqui o seu conteúdo do curso")),
                (
                    "image_slider",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="sliders", to="courses.cursopage"
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]