import uuid
from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class BaseTimestampedModel(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
