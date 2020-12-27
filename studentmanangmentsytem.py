class stu_man_sis:
    def name_input(self, name, surname):
        self.name = name
        self.surname = surname
        self.checkin = False
        for i in range(3):
            name = input("First Name : ")
            surname = input("Surname : ")
            if name == self.name and surname == self.surname:
                print("Welcome", surname.upper(), name)
                self.checkin = True
                break
            else:
                if i == 2:
                    print("Please try again later")
                else:
                    print("Incorrect name")
    def course_reg(self):
        self.courses = ["Design101, Design Management, CAD Modeling, Fundamentals of Art"]
        courseslist = ["Design101", "Design Management", "CAD Modeling", "Fundamentals of Art", "Technical Drawing"]
        for x in enumerate(courseslist,1):
            print(x)
        print("You can register for at least 3 the most 5 courses")
        numberofcourse = int(input( "Number of courses you will register : "))
        if numberofcourse < 3 or course_num > 5
            return 
        else:


    
        