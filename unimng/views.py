from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Professor, Department, Course, Period, Time_Block, Classroom, Schedule

# Create your views here.

# view para el indice o la primer pagina


class IndexView(generic.ListView):
    template_name = 'unimng/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.all()

# view para los cursos


class CourseView(generic.DetailView):
    model = Course
    template_name = 'unimng/course.html'

# view para los professores


class ProfessorList(generic.ListView):
    template_name = 'unimng/professors.html'
    context_object_name = 'professor_list'

    def get_queryset(self):
        return Professor.objects.all()

# detail view para los profesores


class ProfessorDetail(generic.DetailView):
    model = Professor
    template_name = 'unimng/professor.html'

# detail view para los horarios


class ScheduleDetail(generic.DetailView):
    model = Schedule
    template_name = 'unimng/schedule.html'
