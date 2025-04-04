from django.contrib import admin
from .models import *

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'matricula', 'data_nascimento']
    search_fields = ['nome', 'email', 'matricula']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'formacao']
    search_fields = ['nome', 'email']

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'get_professores', 'get_materias' ]
    search_fields = ['nome']
    filter_horizontal = ['alunos']

    def get_professores(self, obj):
        return ", ".join([turma.professor.nome for turma in obj.turma_materias.all()])
    get_professores.short_description = 'Professores'

    def get_materias(self, obj):
        return ", ".join([turma.materia.nome for turma in obj.turma_materias.all()])
    get_materias.short_description = 'Matérias'

@admin.register(TurmaMateria)
class TurmaMateriaAdmin(admin.ModelAdmin):
    list_display = ['turma', 'materia', 'professor']
    list_filter = ['turma', 'materia', 'professor']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'get_turma', 'get_materia', 'nota', 'data_avaliacao']
    search_fields = ['aluno__nome', 'turma_materia__turma__nome']
    list_select_related = ['turma_materia__turma', 'aluno']

    def get_turma(self, obj):
        return obj.turma_materia.turma.nome
    get_turma.short_description = 'Turma' 

    def get_materia(self, obj):
        return obj.turma_materia.materia.nome
    get_materia.short_description = 'Materia'


