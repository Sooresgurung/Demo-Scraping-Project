from django.db import models

# Create your models here.
class ScrapIpo(models.Model):
     symbol = models.CharField(max_length=200)
     company = models.CharField(max_length=200)
     sectors = models.CharField(max_length=200)
     units = models.CharField(max_length=200)
     amount = models.CharField(max_length=200)
     application_date = models.CharField(max_length=200)
     date_of_sebon = models.CharField(max_length=200)
     issue_manager = models.CharField(max_length=200)
     remark = models.CharField(max_length=200)

     def save(self, *args, **kwargs):
        current_amount = self.amount
        max_amount = ScrapIpo.objects.aggregate(models.Max('amount'))['amount__max']

        if not max_amount or current_amount > max_amount:
            max_amount = current_amount

        super().save(*args, **kwargs)
    
     def __str__(self):
         return self.symbol

    


                 