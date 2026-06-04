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