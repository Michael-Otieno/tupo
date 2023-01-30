# Generated by Django 4.1.5 on 2023-01-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('life skills', 'Life skills'), ('children with disabilities', 'Children with disabilities'), ('creative arts', 'Creative arts'), ('sport programs', 'Sport programs')], default=('children with disabilities', 'Children with disabilities'), max_length=200),
        ),
    ]
