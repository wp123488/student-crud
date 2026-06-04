from database import SessionLocal
from models import Student


def create_student(name, age):
    db = SessionLocal()

    student = Student(
        name=name,
        age=age
    )

    db.add(student)

    db.commit()

    db.close()
  def get_students():
    db = SessionLocal()

    students = db.query(Student).all()

    for student in students:
        print(
            student.id,
            student.name,
            student.age
        )

    db.close()
  def update_student(student_id, name):
    db = SessionLocal()

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if student:
        student.name = name
        db.commit()

    db.close()