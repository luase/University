from django.contrib import admin
from .models import Professor, Department, Course, Period, Time_Block, Classroom, Schedule
# Register your models here.
admin.site.register(Professor)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Period)
admin.site.register(Time_Block)
admin.site.register(Classroom)
admin.site.register(Schedule)
