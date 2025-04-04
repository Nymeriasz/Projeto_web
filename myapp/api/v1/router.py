from rest_framework.routers import DefaultRouter
from .viewsets import *

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'turmas&materias', TurmaMateriaViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = router.urls