from django.db import models
from django.forms import ModelForm

# Create your models here.
Gender=(("f","Female"),("m","Male"))

Age=(("15","15"),("16","16"),("17","17"),("18","18"),("19","19"),("20","20"),("21","21"),("22","22"))

failures=(("0","None"),("1","1"),("2","2"),("3","3"),("4","More than 4"))

Pstatus=(("A","Apart"),("T","together"))

Dalc=(("1","Very Low"),("2","Low"),("3","Average"),("4","High"),("5","Very High"))

Higher=(("y","Yes"),("n","No"))

famrel=(("1","Very bad"),("2","Bad"),("3","Neutral"),("4","Good"),("5","Very Good"))

class PredictModel(models.Model):
	student_id = models.CharField(max_length = 15)
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200) 
	gender = models.CharField(max_length=1, choices=Gender)
	age = models.CharField(max_length=2,choices = Age)
	failures = models.CharField(max_length=1,choices = failures)
	pstatus = models.CharField(max_length=1,choices = Pstatus)
	dalc = models.CharField(max_length=1,choices = Dalc)
	higher = models.CharField(max_length=1,choices = Higher)
	famrel = models.CharField(max_length=1,choices = famrel)
	G1 = models.DecimalField(max_digits=5, decimal_places=2)
	G2 = models.DecimalField(max_digits=5, decimal_places=2)
	G3 = models.FloatField()
	def __str__(self): 
		return self.title 