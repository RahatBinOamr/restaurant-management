from django.db import models
from tinymce.models import HTMLField  
from autoslug import AutoSlugField
from django.db.models import Avg
# Create your models here.
PERIOD_CHOICES =(
  ('BREAK_FIST','BRAKE_FIST'),
  ('LUNCH','LUNCH'),
  ('DINNER','DINNER')
)
class Item(models.Model):
  name = models.CharField(max_length=300)
  description = HTMLField() 
  price = models.DecimalField(max_digits=5,decimal_places=2)
  image = models.ImageField(upload_to='items')
  period = models.CharField(max_length=10,choices=PERIOD_CHOICES)
  slug = AutoSlugField(populate_from='name')
  created = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return f"{self.name}"
  
  def average_rating(self):
        average = int(self.review_set.aggregate(Avg('rating'))['rating__avg'])
        return average if average is not None else 0 
  


class Review(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  message = models.TextField()
  rating = models.IntegerField(null=True, blank=True)
  item = models.ForeignKey(Item,models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name}-{self.email}"
  


  

