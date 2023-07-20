from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Photo(models.Model):
    MAX_DESC_LEN = 300
    MIN_DESC_LEN = 10
    MAX_LOC_LEN = 30

    photo = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size,
        )
    )
    description = models.TextField(
        max_length=MAX_DESC_LEN,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(MIN_DESC_LEN),
        )
    )
    location = models.CharField(
        max_length=MAX_LOC_LEN,
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
    date_of_publication = models.DateField(
        auto_now=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
