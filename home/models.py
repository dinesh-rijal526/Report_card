from django.db import models

# Create your models here.

class StudentID(models.Model):
    student_id = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.student_id


class Subject(models.Model):
    subject = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.subject

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.OneToOneField(StudentID,related_name='studentid', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True, unique=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "student"

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name='studentmarks', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} {self.subject.subject}"

    class Mete:
        unique_together = ['student', 'marks']

class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name='studentreportcard', on_delete=models.CASCADE)
    rank = models.IntegerField()
    data_of_report_card = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['rank', 'data_of_report_card']
