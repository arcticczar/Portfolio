# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class PersonalInfo(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=250)
    Street_Address = models.CharField(max_length=250)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Zip_Code = models.IntegerField()
    Phone_Number = models.BigIntegerField()
    Email = models.EmailField()
    Website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name

schedule = (('FT','Full Time'),('PT','Part Time'),('Temp','Temporary'),('Term','Term'), ('other','other'))

class WorkHistory(models.Model):
    Person = models.ForeignKey(PersonalInfo)
    Employer= models.CharField(max_length=200)
    Job_Title= models.CharField(max_length=200)
    Start_Date=models.DateField(blank=True,null=True)
    End_Date=models.DateField(blank=True,null=True)
    Schedule = models.CharField(max_length=50, choices=schedule)
    Starting_Salary = models.BigIntegerField(null=True, blank=True)
    Ending_Salary = models.BigIntegerField(null=True, blank=True)
    Position_Description = models.TextField()
    Supervisor_First_Name = models.CharField(max_length=200, blank=True, null=True)
    Supervisor_Last_Name = models.CharField(max_length=200, blank=True, null=True)
    Supervisor_Phone = models.BigIntegerField(blank=True, null=True)
    Supervisor_Email = models.EmailField(blank=True, null=True)
    Notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.Employer + ' ' + self.Job_Title

    def get_absolute_url(self):
        return reverse('WorkHistory', kwargs={'Employer':self.Employer, 'Job_Title':self.Job_Title})

    def get_update_url(self):
        return reverse('WorkHistory_update', kwargs={'Employer':self.Employer, 'Job_Title':self.Job_Title})

    def get_delete_url(self):
        return reverse( 'WorkHistory_delete', kwargs={'Employer':self.Employer, 'Job_Title':self.Job_Title})

class Volunteer(models.Model):
    Person = models.ForeignKey(PersonalInfo)
    Organization = models.CharField(max_length = 200)
    Start_Date = models.DateField(null=True,blank=True)
    End_Date = models.DateField(null=True,blank=True)
    Work_Performed = models.TextField(blank=True, null=True)
    Achievements = models.TextField(blank=True, null=True)
    Supervisor_First_Name = models.CharField(max_length=200, blank=True, null=True)
    Supervisor_Last_Name = models.CharField(max_length=200, blank=True, null=True)
    Supervisor_Phone = models.BigIntegerField(blank=True, null=True)
    Supervisor_Email = models.EmailField(blank=True, null=True)
    Notes = models.TextField(blank=True, null=True)


class Community(models.Model):
    Person = models.ForeignKey(PersonalInfo)
    Organization = models.CharField(max_length=200)
    Start_Date = models.DateField(blank=True, null=True)
    End_Date = models.DateField(blank=True, null=True)
    Position = models.CharField(max_length=200)
    Achievements = models.TextField(blank=True, null=True)


proficiency = (('B','Beginner'),('I','Intermediate'),('A','Advanced'),('E','Expert'), ('O', 'Other'))

class Skills(models.Model):
    Person = models.ForeignKey(PersonalInfo)
    Description = models.CharField(max_length=200)
    Proficiency_Level = models.CharField(max_length=100, choices = proficiency)
    Notes=models.TextField(blank=True, null=True)

class Certifications(models.Model):
    Person = models.ForeignKey(PersonalInfo)
    Description = models.CharField(max_length=200)
    Proficiency_Level = models.CharField(max_length=100, choices = proficiency)
    Start_Date = models.DateField(blank=True,null=True)
    Expiration_Date=models.DateField(blank=True,null=True)
    Notes=models.TextField(blank=True, null=True)

class Education(models.Model):
    Person = models.ForeignKey(PersonalInfo)
    Institution = models.CharField(max_length=200)
    Street_Address = models.CharField(max_length=250, null=True, blank=True)
    City = models.CharField(max_length=200, null=True, blank=True)
    State = models.CharField(max_length=200, null=True, blank=True)
    Zip_Code = models.IntegerField(null=True, blank=True)
    Start_Date=models.DateField(blank=True,null=True)
    End_Date=models.DateField(blank=True,null=True)
    Subject = models.CharField(max_length=200)
    Completed = models.BooleanField()
    GPA = models.FloatField()
    Link = models.URLField( max_length=250, null=True, blank=True)


class CoverLetter(models.Model):
    Person = models.ForeignKey(PersonalInfo)
    Body = models.TextField()
    Company = models.CharField(max_length = 200)
    Position = models.CharField(max_length = 200)
    Date = models.CharField(max_length = 200)


class Reference(models.Model):
    Person = models.ForeignKey(PersonalInfo)
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=250)
    Street_Address = models.CharField(max_length=250, null=True, blank=True)
    City = models.CharField(max_length=200, null=True, blank=True)
    State = models.CharField(max_length=200, null=True, blank=True)
    Zip_Code = models.IntegerField(null=True, blank=True)
    Phone_Number = models.BigIntegerField( null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Type = models.CharField(max_length=50, choices=(('Pro', 'Professional'), ('Per', 'Personal'),('Both', 'Both'),('Other','Other')))

class Publication(models.Model):
    Person = models.ForeignKey(PersonalInfo)
    Title = models.CharField(max_length=250)
    Authors = models.TextField()
    Type = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=200)
    Pub_City = models.CharField(max_length=200)
    Pub_Year = models.IntegerField()
    Volume = models.CharField(max_length=200,null=True,blank=True)
    Issue = models.CharField(max_length=200, null=True, blank=True)
    Pages = models.CharField(max_length=200, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
