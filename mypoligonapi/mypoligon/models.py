from django.db import models

# Create your models here.
class Poligon(models.Model):
    number_points= models.PositiveIntegerField(blank=True, default=0)
    distance = models.PositiveIntegerField(blank=True, default=0)
    def __str__(self):
	    return str(self.id)

class Points(models.Model):
    poligon_id = models.ForeignKey(Poligon,on_delete=models.CASCADE)
    point_x = models.DecimalField(blank=True, default=0,max_digits=14,decimal_places=2)
    point_y = models.DecimalField(blank=True, default=0,max_digits=14,decimal_places=2)
    def __str__(self):
	    return str(self.id)