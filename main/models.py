from django.db import models
from datetime import date
from django.forms import DateField
from django.urls import reverse


class AbstractHuman(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()

    class Meta: 
        abstract = True 

    def get_age():
        today = date.today
        birth_date = birth_date
        current_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return current_age
 


class Worker(AbstractHuman):
    work_position = models.CharField(max_length=50)
    experience = models.DateField() 

    def get_absolute_url(self): 
        return f"/workers/{self.name}/"
    
    def __str__(self):
        return self.name


class Document(models.Model): 
    worker = models.OneToOneField(Worker, on_delete= models.CASCADE)
    inn = models.CharField(max_length=14)
    card_id = models.CharField(max_length=10)

    def save(self):
        print(f'Сотрудник {Worker.name} сохранен') 
        super(Document, self).save()


class Project(models.Model):
    name = models.CharField(max_length=20)
    worker = models.ManyToManyField(Worker, through='Membership') 

class Membership(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_joined = models.DateField() 

class Customer(AbstractHuman):
    address = models.CharField(max_length=50) 
    phone = models.CharField(max_length=50)


class VIPCustomer(AbstractHuman):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField() 
  

