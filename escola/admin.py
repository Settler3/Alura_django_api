from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class ListandoAlunos(admin.ModelAdmin):
    list_display=('id', 'nome', 'rg', 'data_nascimento')
    list_display_links=('nome', 'data_nascimento')
    search_fields=('nome',)
    list_per_page=10

class ListandoCursos(admin.ModelAdmin):
    list_display=('id', 'codigo_curso', 'nivel')
    list_display_links=('codigo_curso', )
    search_fields=('codigo_curso',)
    list_filter = ("codigo_curso",)
    list_editable = ("nivel",)
    list_per_page=10

class ListandoMatriculas(admin.ModelAdmin):
    list_display=('id', 'aluno', 'curso', 'periodo')
    list_display_links=('id', )
    search_fields=('curso',)
    list_editable = ("periodo",)
    list_per_page=10


# Register your models here.
admin.site.register(Aluno, ListandoAlunos)
admin.site.register(Curso, ListandoCursos)
admin.site.register(Matricula, ListandoMatriculas)