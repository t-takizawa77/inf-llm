from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Question
from .tasks import process_question_data


@receiver(post_save, sender=Question)
def trigger_backend_task(sender, instance, created, **kwargs):
    print(f"post_save signal triggered for question id: {instance.id}")
    if created:
        results = process_question_data(instance.id)
