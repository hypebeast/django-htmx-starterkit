from django.db import models
from django.contrib.auth import get_user_model

from core.database.models import BaseTimestampedModel

User = get_user_model()


class Task(BaseTimestampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField()
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{}".format(self.name)
