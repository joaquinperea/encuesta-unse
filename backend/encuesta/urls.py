"""Urls for the encuesta app."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurveyViewSet, QuestionViewSet, AnswerViewSet, ReorderQuestionAPIView

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='survey')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'answers', AnswerViewSet, basename='answer')

urlpatterns = [
    path('api/', include(router.urls)),
    path('survey/<int:survey_id>/question/<int:question_id>/reorder/', ReorderQuestionAPIView.as_view(), name='reorder_question'),
]
