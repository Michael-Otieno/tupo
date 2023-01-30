from django.db import models

# Create your models here.

class Course(models.Model):
  CATEGORIES = (
    ('LF','Life skills'),
    ('CD','Children with disabilities'),
    ('CA','Creative arts'),
    ('SP','Sport programs'),
  )
  photo = models.ImageField(upload_to='img',default="",blank=True)
  title = models.CharField(max_length=255)
  category = models.CharField(choices=CATEGORIES, default=CATEGORIES[1], max_length=200)
  description = models.CharField(max_length=500)
  content = models.TextField()
  class Meta:
    ordering = ['id']

  def __str__(self):
    return self.title





