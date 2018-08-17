from django.db import models


class Register(models.Model):
    pass

    def __str__(self):
        return self.id
