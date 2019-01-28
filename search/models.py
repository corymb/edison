from django.db import models


class Line(models.Model):
    SEARCHABLE_FIELDS = ('nick', 'recipient', 'message')

    sent = models.DateTimeField()
    nick = models.CharField(max_length=30)
    recipient = models.CharField(null=True, max_length=30)
    message = models.CharField(max_length=512)  # limit set in rfc 2812
    # I would actually use a GIN Index for the message field, but this is fine
    # for the volume of data we have.

    def __str__(self):
        return '{}'.format(self.message)

    class Meta:
        indexes = [
            models.Index(fields=['nick', 'recipient', 'message']),
        ]
