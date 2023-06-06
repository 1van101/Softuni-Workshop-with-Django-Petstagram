from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    MAX_COMM_LEN = 300

    text = models.TextField(
        max_length=MAX_COMM_LEN,
    )
    datetime_of_publication = models.DateTimeField(
        auto_now_add=True,

    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-datetime_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,

    )
