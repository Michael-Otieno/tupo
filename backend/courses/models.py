from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.


class CustomeUserManager(BaseUserManager):
  def create_user(self, email, password, **extra_fields):
    if not email:
      raise ValueError('The Email must be set')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')
    return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  id_number = models.CharField(max_length=200)
  phone_number = models.CharField(max_length=20)
  email = models.CharField(max_length=255,unique=True)
  password = models.CharField(max_length=255)
  username = None

  objects = CustomeUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.email



class Course(models.Model):
  CATEGORIES = (
    ('life skills','Life skills'),
    ('children with disabilities','Children with disabilities'),
    ('creative arts','Creative arts'),
    ('sport programs','Sport programs')
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





