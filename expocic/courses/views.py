from django.views.generic import TemplateView
from .models import CursoPage


class CursoView(TemplateView):
    template_name = 'cursos/curso.html'  # Nome do seu template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtenha o curso_slug da URL
        curso_slug = self.kwargs.get('curso_slug')
        # Consulte o banco de dados para obter os dados do curso com base no curso_slug
        curso = CursoPage.objects.get(curso_slug=curso_slug)
        # Adicione os dados do curso ao contexto
        context['curso'] = curso
        return context
