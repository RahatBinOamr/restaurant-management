from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  subject = models.CharField(max_length=200)
  message = models.TextField()


  def __str__(self):
    return f"{self.name}-{self.email}"
  


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField()
    people = models.IntegerField(choices=[(i, f'People {i}') for i in range(1, 4)])
    special_request = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.name} - {self.datetime}"
    

PERIOD_CHOICES =(
  ('BREAK_FIST','BRAKE_FIST'),
  ('LUNCH','LUNCH'),
  ('DINNER','DINNER')
)
class Item(models.Model):
  name = models.CharField(max_length=300)
  description = models.TextField()
  price = models.DecimalField(max_digits=5,decimal_places=2)
  image = models.ImageField(upload_to='items')
  period = models.CharField(max_length=10,choices=PERIOD_CHOICES)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name}"

