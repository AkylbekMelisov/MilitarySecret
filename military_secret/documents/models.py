from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    secret_level = models.CharField(choices=(
        ('public', 'public'),
        ('private', 'private'),
        ('secret', 'secret'),
        ('top-secret', 'top-secret'),
        ('super-secret', 'super-secret')
    ), max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=(
        ('active', 'active'),
        ('dead', 'dead')
    ), max_length=7, default='active')
