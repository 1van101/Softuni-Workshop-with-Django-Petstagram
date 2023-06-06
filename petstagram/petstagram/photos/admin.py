from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class AdminPhotos(admin.ModelAdmin):
    list_display = ('pk', 'date_of_publication', 'tagged')

    def tagged(self, current_photo_obj):
        tagged_pets = current_photo_obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join([p.name for p in tagged_pets])
        return 'Empty list'
