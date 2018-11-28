from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Professor, Department, Course, Period, Time_Block, Classroom, Schedule

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'unimng/index.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.all()
