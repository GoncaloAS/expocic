from django.db import models
from django.utils.text import slugify
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel


class Sliders(Orderable):
    page = ParentalKey("CursoPage", related_name="sliders")
    image_slider = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Image'
    )
    title_slider = models.CharField(max_length=100)
    paragraph_slider = RichTextField(default='Insira aqui o conteúdo do curso')


class CursoPage(Page):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    curso_slug = models.SlugField(unique=True)

    content_panels = Page.content_panels + [
        FieldPanel('titulo'),
        FieldPanel('descricao'),
        FieldPanel('curso_slug'),
        MultiFieldPanel(
            [InlinePanel("sliders", label="Sliders")],
            heading="Sliders",
        ),
    ]

    def save(self, *args, **kwargs):
        if not self.curso_slug:
            self.curso_slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    max_count = 1
