from django.db import models


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_answered = models.BooleanField(default=False)
    is_corrected = models.BooleanField(default=False)
    chat = models.ForeignKey(
        Chat,
        null=True,
        related_name="questions",
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        print(getattr(self, 'chat_id'))
        if not getattr(self, 'chat_id', None):
            self.chat = Chat.objects.create()
        elif not self.chat:
            self.chat = Chat.objects.create()
        super().save(*args, **kwargs)


class Answer(models.Model):
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(
        Question,
        related_name="answers",
        on_delete=models.CASCADE
    )
