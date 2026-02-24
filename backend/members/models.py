from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='members/', null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
        