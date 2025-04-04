from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from myapp.base_model import *
from decimal import Decimal

class Aluno(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"

class Professor(BaseModel):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    formacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Materia(BaseModel):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Turma(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    alunos = models.ManyToManyField(Aluno, related_name="turmas")

    def __str__(self):
        return self.nome

class TurmaMateria(BaseModel):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="turma_materias")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['turma', 'materia', 'professor'],
                name='unique_turma_materia_professor',    
            )
        ]

    def __str__(self):
        return f"{self.turma.nome} - {self.materia.nome} (Prof. {self.professor.nome})"
    
class Avaliacao(BaseModel):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="avaliacoes")
    turma_materia = models.ForeignKey(TurmaMateria, on_delete=models.CASCADE, related_name="avaliacoes", null=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('10'))])
    data_avaliacao = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['aluno', 'turma_materia'],
                name = 'avaliacao_unica_por_aluno_turma'
            )
        ]

    def __str__(self):
        return f"Avaliação de {self.aluno.nome} - {self.turma_materia.materia.nome}"

