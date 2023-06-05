from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class List(models.Model):
    name = models.CharField(
        max_length=63,
        blank=False,
        null=False,
        unique=True
    )

    def get_absolute_url(self):
        return reverse_lazy("listindex")
    
    def __str__(self):
        return self.name
    
class Todo(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False
    )

    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False
    )

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    dueDate = models.DateField(
        blank=True,
        null=True
    )

    dueTime = models.TimeField(
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=False
    )

    list = models.ForeignKey(
        List,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse_lazy("tododetail", args=[self.id])

    def __str__(self):
        return self.title
    