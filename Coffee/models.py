from django.db import models

class Coffee(models.Model):
  name = models.CharField(max_length = 75)
  roaster = models.CharField(max_length = 75)
  variety = models.CharField(max_length = 50)
  brew_method = models.CharField(max_length = 50)
  tasting_notes = models.TextField(default = 'Red fruits, berries, etc.')

  def __str__(self):
    return self.name