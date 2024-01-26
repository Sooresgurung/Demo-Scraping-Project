from django.db import models

# Create your models here.
class ScrapData(models.Model):
     symbol = models.CharField(max_length=200)
     turnover = models.CharField(max_length=200)
     ltp = models.CharField(max_length=200)
     change = models.CharField(max_length=200)
     high = models.CharField(max_length=200)
     low = models.CharField(max_length=200)
     open = models.CharField(max_length=200)
     qty = models.CharField(max_length=200)

     def save(self, *args, **kwargs):
        current_turnover = self.turnover
        max_turnover = ScrapData.objects.aggregate(models.Max('turnover'))['turnover__max']

        if not max_turnover or current_turnover > max_turnover:
            max_turnover = current_turnover

        super().save(*args, **kwargs)
     
     def __str__(self):
         return self.symbol