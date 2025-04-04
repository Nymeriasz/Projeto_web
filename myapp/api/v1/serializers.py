from rest_framework import serializers
from myapp.models import *

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
    
class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    alunos = AlunoSerializer(many=True, read_only=True)

    alunos_ids = serializers.PrimaryKeyRelatedField(
        queryset=Aluno.objects.all(),  
        source='alunos', 
        many=True,
        write_only=True, 
        required=False 
    )
    
    class Meta:
        model = Turma
        fields = '__all__'

class TurmaMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurmaMateria
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
    aluno = AlunoSerializer(read_only=True)

    aluno_id = serializers.PrimaryKeyRelatedField(
        queryset = Aluno.objects.all(),
        source ='aluno',
        write_only=True,
        required = True
    )
    class Meta:
        model = Avaliacao
        fields = '__all__'