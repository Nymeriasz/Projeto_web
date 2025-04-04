from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from myapp.models import *
from .serializers import *

class AlunoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class TurmaMateriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = TurmaMateria.objects.all()
    serializer_class = TurmaMateriaSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
