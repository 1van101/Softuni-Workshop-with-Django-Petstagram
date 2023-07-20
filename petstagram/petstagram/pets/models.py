from django.db import models
from django.utils.text import slugify

from petstagram.accounts.models import PetstagramUser
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Pet(models.Model):
    MAX_LENGTH = 30

    name = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
    )
    personal_photo = models.URLField(
        null=False,
        blank=False,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.pk} {self.name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk} - {self.name}'
