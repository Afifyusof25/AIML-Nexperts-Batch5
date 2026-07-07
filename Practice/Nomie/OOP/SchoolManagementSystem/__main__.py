import models
import manager

print("Welcome to the School Management System")


while True:
    print("----------------------------")
    print("1 - to Add Student")
    print("2 - to View Student")
    print("3 - to Add Teacher")
    print("4 - to View Teacher")
    print("q - to Exit")

    choice = input("enter choice : ")

    if choice == "1":
        manager.add_student()
    
    elif choice == "2":
        manager.display_students()
    
    elif choice == "3":
        manager.add_teacher()
    
    elif choice == "4":
        manager.display_teachers()
    
    elif choice == "q":
        break

    else:
        print("Invalid Choice")


