from django.db import models

# Create your models here.
class OrderContactInfo(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  phone = models.CharField(max_length=20)
  address = models.TextField()
  session_key = models.CharField(max_length=200, blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name}-{self.email}-{self.phone}-{self.address}"
