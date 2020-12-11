from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    isRed =  models.BooleanField(default=False)
    logo = models.ImageField(null = True)


    def __str__(self):
        return self.name

# class Group(models.Model):
#     teams = models.ForeignKey(Team, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.team.
