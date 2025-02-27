"""Views for the encuesta app."""

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Survey, Question, Answer
from .serializers import SurveySerializer, QuestionSerializer, AnswerSerializer
from .services import insert_question_at


class SurveyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Survey model."""
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Question model."""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Answer model."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ReorderQuestionAPIView(APIView):
    """API view to reorder a question in a survey."""
    def patch(self, request, survey_id, question_id):
        """Change the position of a question in a survey."""
        try:
            question = Question.objects.get(id=question_id, survey_id=survey_id)
        except Question.DoesNotExist:
            return Response({'error': 'Pregunta no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        new_position = request.data.get('new_position')

        if not new_position:
            return Response(
                {'error': 'Se debe proporcionar la nueva posición'},
                status=status.HTTP_400_BAD_REQUEST
            )

        insert_question_at(survey_id, question, new_position)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
