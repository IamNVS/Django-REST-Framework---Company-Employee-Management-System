from django.db import models

# Create your models here.
# Creating compay modele
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    company_location = models.CharField(max_length=50)
    company_about = models.TextField()
    type = models.CharField(max_length=100, choices=(("IT","IT"),
                                                    ("NonIT", "NonIT"),
                                                    ("Mobiles", "Mobiles")))
    added = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.company_name +" "+ self.company_location

# Creating employee modele
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_email = models.CharField(max_length=50)
    employee_phone = models.CharField(max_length=10)
    employee_about = models.TextField()
    employee_position = models.CharField(max_length=50,choices=(
        ("Manager", "manager"),
        ("HR", "HR"),
        ("Software Developer","Software Developer"),
        ("Team Lead", "Team Lead")
    ) )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    
