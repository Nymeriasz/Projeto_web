from django.db import models
from myapp.base_model import BaseModel

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

class Turma(BaseModel):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="turmas")
    alunos = models.ManyToManyField(Aluno, related_name="turmas")

    def __str__(self):
        return self.nome
    
class Avaliacao(BaseModel):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="avaliacoes")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="avaliacoes")
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    data_avaliacao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Avaliação de {self.aluno.nome} - {self.turma.nome}"

