from django.contrib import admin
from .models import Aluno, Professor, Turma, Avaliacao

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'matricula']
    search_fields = ['nome', 'email']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'formacao']
    search_fields = ['nome', 'email']

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'professor']
    search_fields = ['nome']
    filter_horizontal = ['alunos']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'turma', 'nota', 'data_avaliacao']
    search_fields = ['aluno__nome', 'turma__nome']
