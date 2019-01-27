from django.db import models


class Line(models.Model):
    sent = models.DateTimeField()
    nick = models.CharField(max_length=30)
    recipient = models.CharField(null=True, max_length=30)
    message = models.CharField(max_length=512)  # limit set in rfc 2812
