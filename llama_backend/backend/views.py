from rest_framework import viewsets
from rest_framework.response import Response
from .models import Chat, Question, Answer
from .serializer import ChatSerializer, QuestionSerializer, AnswerSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        # ????????????????????????????????????????????????????????????
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.save()

        # ????????????????????????????????????
        response_data = {
            "chat_id": question.chat_id,
            "message": "Question created successfully"
        }
        return Response(response_data, status=201)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
