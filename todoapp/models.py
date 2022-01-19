from django.db import models


class task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse("task", args=[str(self.id)])