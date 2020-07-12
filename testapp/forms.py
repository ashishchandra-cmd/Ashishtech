from django import forms
from testapp.models import Course_table  ,StudentEnrollCourse

class Course_tableForm(forms.ModelForm):
    class Meta:
        model=Course_table
        fields=['id','Course_Name','Faculty','class_date','class_time','Fee','Duration']


class StudentEnrollCourseForm(forms.ModelForm):
    class Meta:
        model=StudentEnrollCourse
        fields=['Name','phone']

