from django.db import models

# Create your models here.
class Leader(models.Model):
    full_name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    message = models.TextField()
    profile_picture = models.ImageField(upload_to='leaders/')

    def __str__(self):
        return f"{self.full_name} - {self.position}"
        