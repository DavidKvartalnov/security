import uuid
from django.db import models


class Person(models.Model):
    data = models.CharField(max_length=1024)
    pin = models.CharField(max_length=16)
    unique_value = models.UUIDField(default=uuid.uuid4())


