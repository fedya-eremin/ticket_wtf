from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from datetime import datetime, timezone


def get_datetime() -> datetime:
    return datetime.now(timezone.utc)


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.TextField("title", null=False, blank=False)
    description = models.TextField("description", null=False, blank=False)
    phone = models.TextField("phone", null=False, blank=False)

    class Status(models.TextChoices):
        CREATED = "created", "created"
        IN_WORK = "in work", "in work"
        DONE = "done", "done"

    status = models.TextField(
        "status", choices=Status, null=False, blank=False, default=Status.CREATED
    )

    status = models.TextField("status", choices=Status, null=False, blank=False)
    created = models.DateTimeField(
        "created",
        default=get_datetime,
        null=True,
        blank=True,
    )
