from django.contrib.auth.models import Permission, User
from django.db import models


class Department(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.DO_NOTHING)
    sec_name = models.CharField(max_length=20)
    Depart_name = models.CharField(max_length=20)
    No_sub=models.IntegerField(default=30)
    def __str__(self):
        return self.Depart_name + ' - ' + self. sec_name
class Student(models.Model):
     department = models.ForeignKey(Department,on_delete=models.CASCADE)
     name = models.CharField(max_length=100)
     roll_no=models.IntegerField(default=30)
     sub1_marks =models.IntegerField(default=10)
     sub1_attaindance =models.IntegerField(default=10)
     sub2_marks =models.IntegerField(default=10)
     sub2_attaindance =models.IntegerField(default=10)
     sub3_marks =models.IntegerField(default=10)
     sub3_attaindance =models.IntegerField(default=10)
     def __str__(self):
        return str(self.roll_no)
     # def __init__(self):
     #    return self.roll_no

# class Subject(models.Model):
#      student = models.ForeignKey(Student, on_delete=models.CASCADE)
#      marks=models.IntegerField(default=10)
#      max_attendance=models.IntegerField(default=10)
#      sub_attendance =models.IntegerField(default=10)
#      # def __str__(self):
#      #     return self. marks + ' - ' + self.sub_attendance

