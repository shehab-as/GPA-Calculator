import json
import Student
import Help
                #~~~~~~~~~~~~~~~~~~~~ Main Program ~~~~~~~~~~~~~~~~~~~~#
print("Playing around with Python 3.5.2 ... So here is a GPA Calculator!")
while True:
    print("What do you want to do?")
    print("1) Create Profile")
    print("2) Edit Profile")
    print("3) Help")
    print("4) Exit")

    reply = int(input("->"))

    ###############################################################
    if reply == 1:
        ######### Create Profile #########
        print("="*25)
        print("~~~ New Profile ~~~")
        name = input("->Profile Name:")
        S = Student.Student(name)
        while True:
            print("1- Add Grade\n"
                  "2- Remove Grade\n"
                  "3- Show GPA\n"
                  "4- Show Credits\n"
                  "5- Show Current Data\n"
                  "6- Show Courses\n"
                  "7- Save and Exit")
            choice = int(input("->"))
            if choice == 1:
                #Add Grade
                print("~~~ Adding Grade ~~~~")
                print("=" * 25)
                Add_CourseName = input("->Course Name:")
                Add_LetterGrade = input("->Course Letter Grade:").upper()
                Add_CreditHR = int(input("->Course Credit Hour:"))
                S.Add_Grade(Add_CourseName, Add_LetterGrade, Add_CreditHR)
                continue

            elif choice == 2:
                #Remove Grade
                print("~~~ Removing Grade ~~~~")
                print("=" * 25)
                Remove_CourseName = input("->Course Name:")
                S.Remove_Grade(Remove_CourseName)
                continue

            elif choice == 3:
                #Show Current GPA
                S.Show_GPA()
                continue

            elif choice == 4:
                #Show Current Total Cr Hours
                S.Show_Total_Credits()
                continue

            elif choice == 5:
                _d = S.retrieve_Student_Data()
                print(_d["Courses"])

            elif choice == 6:
                S.Show_Student_Courses()

            elif choice == 7:
                #Save File to JSON and Exit
                with open('Profile.json', mode='w', encoding='utf-8') as file:
                    json.dump(S.retrieve_Student_Data(), file, indent=2)
                break
        continue
    ###############################################################
    elif reply == 2:
        ######### Edit Profile #########
        with open('Profile.json', mode='r', encoding='utf-8') as file:
            data = json.load(file)

        S = Student.Student(data["Student Name"])
        S.set_Student_Data(data)
        S.GPA = data["Overall GPA"]
        S.CreditCount = data["Credit Hours"]
        S.List_of_Courses = data["Courses"].keys()

        while True:
            print("1- Add Grade\n"
                  "2- Remove Grade\n"
                  "3- Show GPA\n"
                  "4- Show Credits\n"
                  "5- Show Current Data\n"
                  "6- Show Courses\n"
                  "7- Save and Exit")
            choice = int(input("->"))
            if choice == 1:
                #Add Grade
                print("~~~ Adding Grade ~~~~")
                print("=" * 25)
                Add_CourseName = input("->Course Name:")
                Add_LetterGrade = input("->Course Letter Grade:").upper()
                Add_CreditHR = int(input("->Course Credit Hour:"))
                S.Add_Grade(Add_CourseName, Add_LetterGrade, Add_CreditHR)
                continue

            elif choice == 2:
                #Remove Grade
                print("~~~ Removing Grade ~~~~")
                print("=" * 25)
                Remove_CourseName = input("->Course Name:")
                S.Remove_Grade(Remove_CourseName)
                continue

            elif choice == 3:
                #Show Current GPA
                S.Show_GPA()
                continue

            elif choice == 4:
                #Show Current Total Cr Hours
                S.Show_Total_Credits()
                continue

            elif choice == 5:
                _d = S.retrieve_Student_Data()
                print(_d["Courses"])

            elif choice == 6:
                S.Show_Student_Courses()

            elif choice == 7:
                #Save File to JSON and Exit
                with open('Profile.json', mode='w', encoding='utf-8') as file:
                    json.dump(S.retrieve_Student_Data(), file, indent=2)
                break
        continue

    ###############################################################
    elif reply == 3:
        ######### Help #########
        Help.Display()
        continue

    ###############################################################
    elif reply == 4:
        ######### Program Ended #########
        print("Good Bye! :)")
        exit(0)