from faker import Faker
import random
from django.db.models import Sum
from .models import *

fack = Faker()


def seed_db(n) -> None :
    try:
        for _ in range (n) :
            student_id = f"STD-0{random.randint(100, 999)}"
            student_name = fack.name()
            student_email = fack.email()
            student_age = random.randint(18, 25)
            student_address = fack.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                name = student_name,
                student_id = student_id_obj,
                email = student_email,
                age = student_age,
                address = student_address 
            )
        
    except Exception as e:
        print(e)



def create_subject_marks():
    try:
        students = Student.objects.all()
        subjects = Subject.objects.all()
        bulk_list = []

        if not students.exists():
            print("No students found!")
            return

        if not subjects.exists():
            print("No subjects found!")
            return

        for student in students:
            for subject in subjects:
                bulk_list.append(SubjectMarks(
                    student=student,
                    subject=subject,
                    marks=random.randint(0, 100)
                ))

        SubjectMarks.objects.bulk_create(bulk_list, batch_size=500)
        print(f"Created {len(bulk_list)} subject marks entries")

    except Exception as e:
        print(f"Error: {str(e)}")
        raise
         

def generate_report_card():
    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', 'age')
    i = 1
    for rank in ranks :
        ReportCard.objects.create(
            student = rank,
            rank = i
        )
        i = i +1
