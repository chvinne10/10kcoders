from django.db import models
class Student(models.Model):
    student_name=models.CharField(max_length=20)
    age=models.IntegerField()
    
    
    
    