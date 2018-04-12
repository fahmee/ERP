from django import forms
from django.contrib.auth.models import User

from .models import Department,Student


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['sec_name', 'Depart_name', 'No_sub']


class StudentForm(forms.ModelForm):

    class Meta:
        model =Student
        fields = ['name', 'roll_no','sub1_marks','sub2_marks','sub3_marks','sub1_attaindance','sub2_attaindance','sub3_attaindance']


# class SubjectForm(forms.ModelForm):

#     class Meta:
#         model = Subject
#         fields = ['marks','sub_attendance','max_attendance']



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
