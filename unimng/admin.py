from django.contrib import admin
from .models import Professor, Department, Course, Period, Time_Block, Classroom, Schedule
# Register your models here.


class ClassroomAdmin(admin.ModelAdmin):
    def description(self):
        return 'Building ' + self.building
    fields = ['descr', 'building', 'seat_count', 'has_projector']
    list_display = (description, 'descr', 'seat_count', 'has_projector')
    list_filter = ['building', 'has_projector', 'seat_count']

class CourseAdmin(admin.ModelAdmin):
    fields = ['descr', 'code']
    list_display = ('descr', 'code')

class ProfessorInline(admin.TabularInline):
    model = Professor
    extra = 1

class DepartmentAdmin(admin.ModelAdmin):
    fields = ['descr']
    inlines = [ProfessorInline]

class PeriodAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['descr']}),
        ('Date information', {'fields': ['begin_date' ,'end_date']}),
    ]
    list_display = ('descr', 'begin_date', 'end_date')
    list_filter = ['end_date', 'begin_date']

class ProfessorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Professional Information',    {'fields': ['first_name', 'last_name', 'department']}),
        ('Academic Information',        {'fields': ['username' ,'user_passw', 'is_administrator']}),
    ]
    list_display = ('last_name', 'first_name', 'department', 'is_administrator')
    list_filter = ['department', 'is_administrator']

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'professor', 'time_block', 'period')
    list_filter = ['course', 'professor', 'period']

class Time_BlockAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Description',         {'fields': ['descr']}),
        ('Time (minutes past 12:00 am)',                {'fields': ['begin_minute', 'end_minute']}),
        ('Days of the week',    {'fields': ['monday' ,'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']}),
    ]

admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Time_Block, Time_BlockAdmin)
