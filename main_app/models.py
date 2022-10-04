from django.db import models

# Create your models here.
class Keycaps(models.Model):

    name = models.CharField(max_length=150)
    img = models.CharField(max_length=350)
    info = models.TextField(max_length=1000)
    available_keycap = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']