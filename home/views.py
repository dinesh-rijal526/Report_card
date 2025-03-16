from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def home(request):
    queryset = Student.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(name__icontains = search) |
            Q(student_id__student_id__icontains = search)
        ).distinct()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {'students':page_obj}
    return render(request, 'get_student.html', context)



def report_card(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    return render(request, 'report_card.html', {'mark':queryset, 'total_mark': total_marks})