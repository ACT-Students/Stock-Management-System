from django.db import models

CHOICES = (
	("1", "Available"),
	("2", "Not Available")
)
 
class Category(models.Model):
	name = models.CharField(max_length=255,default=1)
	status = models.CharField(max_length=10, choices=CHOICES, default='1')

	def __str__(self):
		return self.name

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='1')
    status = models.CharField(max_length=10, choices=CHOICES, default='1')

    def __str__(self):
	    return self.name