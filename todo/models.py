from django.db import models


class ToDoItem(models.Model):
    content = models.TextField()
