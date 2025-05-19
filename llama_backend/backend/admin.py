from django.contrib import admin
from .models import Chat, Question, Answer


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
