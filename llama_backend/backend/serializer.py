from rest_framework import serializers

from .models import Chat, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'answer_text',
        )


class QuestionSerializer(serializers.ModelSerializer):
    chat = serializers.PrimaryKeyRelatedField(
        queryset=Chat.objects.all(),
        required=False,
        allow_null=True,
    )
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = (
            'question_text',
            'is_answered',
            'is_corrected',
            'chat',
            'answers',
        )
    
    def create(self, validated_data):
        if 'chat' not in validated_data or validated_data['chat'] is None:
            validated_data['chat'] = Chat.objects.create()
        return super().create(validated_data)


class ChatSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ('id', 'questions')
