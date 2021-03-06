from django.db import models


class Opioids(models.Model):
    """SQLAlchemy model for the Psql database
    """
    location_id = models.IntegerField()
    location_name = models.CharField(max_length=1024)
    sex_id = models.IntegerField()
    sex_name = models.CharField(max_length=1024)
    year = models.IntegerField()
    val = models.DecimalField(max_digits=25, decimal_places=20)
    upper = models.DecimalField(max_digits=25, decimal_places=20)
    lower = models.DecimalField(max_digits=25, decimal_places=20)
    rank = models.IntegerField()
    sex_percentage = models.DecimalField(max_digits=25, decimal_places=20)
    percent_change = models.DecimalField(max_digits=25, decimal_places=20)
    average_percent_change = models.DecimalField(max_digits=25, decimal_places=20)
    raw_decrease_from_peak = models.DecimalField(max_digits=25, decimal_places=20)
    raw_increase_from_min = models.DecimalField(max_digits=25, decimal_places=20)
    avg_percent_change_since_peak = models.DecimalField(max_digits=25, decimal_places=20)
    avg_percent_change_since_min = models.DecimalField(max_digits=25, decimal_places=20)
    peak = models.DecimalField(max_digits=25, decimal_places=20)
    min = models.DecimalField(max_digits=25, decimal_places=20)



    def __str__(self):
        return '{}'.format(self.name)
