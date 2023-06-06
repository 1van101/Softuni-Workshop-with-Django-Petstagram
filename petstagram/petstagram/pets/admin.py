from django.contrib import admin

from petstagram.pets.models import Pet


@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
