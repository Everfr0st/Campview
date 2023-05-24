from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Village(models.Model):
    village_name = models.CharField(max_length=100)
    image=models.URLField() 
    minimal_age = models.PositiveIntegerField(validators=[MinValueValidator(4), MaxValueValidator(16)], default=4)
    maximum_age = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(16)], default=10)
    #To keep in mind
    #Grade)? = models.TextChoices('Upper', 'Lower')
    
    def counting_villages_number(self):
        return "There's " + str(Village.objects.count()) + " villages in your camp"


    #This method changes the response when we ask for the object in terminal
    def __str__(self):
        return self.village_name + ", Minimal age: " + str(self.minimal_age) + ", Maximum age: " + str(self.maximum_age)


class Cabain(models.Model):
    #village_lists = [(v.id, v.village_name) for v in Village.objects.all()]
    # belonging_village = models.IntegerField(choices=village_lists, default=0)
    cabain_name = models.CharField(max_length=100)
    cabain_image = models.URLField() 
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    #This method changes the response when we ask for the object in terminal
    def __str__(self):
        return self.cabain_name
    

class Activity(models.Model):
    activity_name = models.CharField(max_length=100)

    def __str__(self):
        return self.activity_name
    

ACTIVITIES_CHOICES = (
    ("Ropes", "Ropes"),
    ("2", "HBR"),
    ("3", "Soccer"),
    ("4", "Pottery"),
    ("5", "Arts"),
    ("6", "Archery")
)

class Camper(models.Model):

    camper_name = models.CharField(max_length=40)
    camper_age = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(16)], default=4)
    camper_image = models.URLField(default="")
    cabain = models.ForeignKey(Cabain, on_delete=models.CASCADE)   
    camper_preference_1 = models.CharField(max_length=50, default='Ropes')
    camper_preference_2 = models.CharField(max_length=50, default='Ropes')
    camper_preference_3 = models.CharField(max_length=50, default='Ropes')
    camper_preference_4 = models.CharField(max_length=50, default='Ropes')

    def __str__(self):
        return f"{self.camper_name} {self.camper_age}"
        


        