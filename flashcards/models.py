from django.db import models

class Flashcard(models.Model):
    title = models.CharField(max_length=120)
    front_text = models.TextField()
    back_text =  models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
