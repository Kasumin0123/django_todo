from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Todo)
class PostAdmin(admin.ModelAdmin):
    pass