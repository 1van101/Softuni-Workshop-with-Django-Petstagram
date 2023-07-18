from django import forms

from petstagram.photos.models import Photo


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class CreatePhotoForm(BasePhotoForm):
    pass


class EditPhotoForm(BasePhotoForm):
    class Meta(BasePhotoForm.Meta):
        exclude = ['photo']
