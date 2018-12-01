from django.db import models
from django.utils import timezone

# Departamento


class Department(models.Model):
    descr = models.CharField(max_length=45)

    def __str__(self):
        return self.descr

# Cursos


class Course(models.Model):
    code = models.CharField(max_length=9)
    descr = models.CharField(max_length=45)

    def __str__(self):
        return self.descr

# Periodo


class Period(models.Model):
    descr = models.CharField(max_length=20)
    begin_date = models.DateTimeField('Begin date')
    end_date = models.DateTimeField('End date')

    def __str__(self):
        return self.descr

# Timeblock


class Time_Block(models.Model):
    descr = models.CharField(max_length=60)
    begin_minute = models.IntegerField()
    end_minute = models.IntegerField()
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    def __str__(self):
        return self.descr

# Salon de clases


class Classroom(models.Model):
    descr = models.CharField(max_length=10, null=True)
    seat_count = models.IntegerField()
    has_projector = models.BooleanField(default=False)
    building = models.CharField(max_length=1)

    def __str__(self):
        return 'Building ' + self.building + ', ' + self.descr

# Profesores/Maestros


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='members')
    username = models.CharField(max_length=20)
    user_passw = models.CharField(max_length=25)
    is_administrator = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Horario


class Schedule(models.Model):
    class Meta:
        unique_together = (
            ('professor', 'course', 'period', 'time_block', 'classroom'))
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name='schedule')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='schedule')
    period = models.ForeignKey(
        Period, on_delete=models.CASCADE, related_name='schedule')
    time_block = models.ForeignKey(
        Time_Block, on_delete=models.CASCADE, related_name='schedule')
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name='schedule')

    def __str__(self):
        return self.professor.first_name + ' ' + self.professor.last_name + ' - ' + self.time_block.descr

    def is_currently_available(self):
        now = timezone.now()
        return self.period.begin_date <= now <= self.period.end_date

    is_currently_available.boolean = True
    is_currently_available.short_description = 'Currently available?'
