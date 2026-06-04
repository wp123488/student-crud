from models import Base
from database import engine
from crud import *

def main():
    Base.metadata.create_all(engine)

    create_student("Tom",18)
    create_student("Jack",20)
    print("查询结果")
    get_students()
    update_student(1,"Tom_New")
    delete_student(2)
    print("最终结果")
    get_students()
    
if__name__== "__main__":
    main()
