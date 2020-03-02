from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

#######################################################################################################################
class Upload_Swigy_Files(models.Model):
    img = models.ImageField(upload_to='picture/%Y/%m/%d/', max_length=255)
    Learning_rate = models.IntegerField(default=1.0)
    epochi_range = models.IntegerField(default=1.0)

#####################################################SOM############################################################################
class som(models.Model):
	SET_OF_CHOICES = (
		('auto', 'Auto'),
		('manual', 'Manual'),)
	Perform_PCA = (
        ('yes', 'Yes'),
        ('no', 'No'),)
	Learning_rate = models.IntegerField(default=1.0)
	Epochi= models.IntegerField(default=1.0)
	standard_Deviation = models.CharField(max_length=250)
	Som_map_column = models.IntegerField(default=1.0)
	Som_map_rows = models.IntegerField(default=1.0)
	set_of_choices = models.CharField(max_length=10,  
                              choices=SET_OF_CHOICES, 
                              default='auto')
	performance_pca = models.CharField(max_length=10,  
                              choices=Perform_PCA, 
                              default='yes')
	def __str__(self):
		return self.performance_pca
    #4.this filed get value automatic	value so it is not visible in the admin panel
#################################################################################################################################      
class clustering(models.Model):

 	INITIALIZER = (
 		('kmeans++', 'Kmeans++'),
 		('random', 'Random'),)
 	ALGORITHM = (
 		('auto', 'Auto'),
 		('full', 'Full'),('elkan', 'Elkan'),)
 	number_of_chusks = models.IntegerField(default=1.0)
 	max_iteration = models.IntegerField(default=1.0)
 	intializer = models.CharField(choices=INITIALIZER, max_length=128)
 	n_init = models.IntegerField(default=10.0)
 	algorithm= models.CharField(max_length=10,  
                              choices=ALGORITHM, 
                              default='auto')
 	Tolerance=models.IntegerField(default=1.0)