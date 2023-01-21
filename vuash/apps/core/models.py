import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    id = models.UUIDField(_("id"), default=uuid.uuid4, primary_key=True)
    data = models.TextField(_("data"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")
        db_table = "messages"

    def __str__(self):
        return self.data
