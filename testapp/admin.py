from django.contrib import admin
from testapp.models import Course_table ,Student_register ,StudentEnrollCourse
# Register your models here.

admin.site.register(Course_table)
admin.site.register( Student_register)
admin.site.register( StudentEnrollCourse)