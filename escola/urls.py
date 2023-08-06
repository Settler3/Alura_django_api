from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, \
    MatriculasViewSet, ListaMatriculasAluno, ListaCursosAluno
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('alunos/<int:id>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:id>/alunos/', ListaCursosAluno.as_view()),
]