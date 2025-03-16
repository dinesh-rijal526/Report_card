from django.contrib import admin
from django.db.models import Sum
from .models import *

# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display = ['student_id', 'name', 'email']
    
class AdminSubjectMarks(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

class AdminReportCard(admin.ModelAdmin):
    list_display = ['student', 'rank', 'total_mark', 'data_of_report_card']
    ordering = ['rank']

    def total_mark(self, obj):
        student_marks = SubjectMarks.objects.filter(student = obj.student )
        marks = student_marks.aggregate(marks = Sum('marks'))
        return marks['marks']

admin.site.register(Student, AdminStudent)
admin.site.register(StudentID)
admin.site.register(Subject)
admin.site.register(SubjectMarks, AdminSubjectMarks)
admin.site.register(ReportCard, AdminReportCard)