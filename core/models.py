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
    


class Subscribe(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class Team(models.Model):
  name = models.CharField(max_length=200)
  image = models.ImageField(upload_to='team_images/')
  designation = models.CharField(max_length=200)
  facebook = models.URLField(null=True, blank=True)
  instagram = models.URLField(null=True, blank=True)
  twitter = models.URLField(null=True, blank=True)

  def __str__(self):
    return f"{self.name}-({self.designation})"
