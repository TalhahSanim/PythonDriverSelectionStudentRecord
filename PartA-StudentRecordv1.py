class Student:
    # as this is a constant dictionary, I declare them in the class.
    GRADE_NUMBERING = {
                   "F": (0,49),
                   "P":(50,59),
                   "C": (60,69),
                   "D": (70,79),
                   "HD": (80,100),
                
                   }
    
#initialize the constructor for students
    def __init__(self, student_id, first_name, last_name, subjects, address):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = subjects
        self.address = address
        
# assigning a grade for a students based on results from subject performance
    # def grade(self):
        # for subject, marks in self.subjects.items():
        #     print(marks)
        #     print(subject)
        #     for grade, (high, low) in self.GRADE_NUMBERING.items():
        #         if low <= marks <= high:
        #             print(low, high, grade)
        #             subject[subject] = grade, marks
        #             #maths = HD, 99
        #             break
        #         print(f"{subject} of marks: {marks} with a grade of {grade}")
            

    def display_info(Student):
        # print(f"First Name: {Student.first_name}")
        # print(f"Last Name: {Student.last_name}")
        # print(f"Student ID: {Student.student_id}  ")
    
        print(f"{Student.first_name}'s file")
        print()
        for subject, marks in Student.subjects.items():
            # print(marks)
            # print(subject)
            for grade, (low, high) in Student.GRADE_NUMBERING.items():
                if low <= marks <= high:
                    # print(f"{subject}, {marks}, {grade}")
                    print(f"{subject} Mark of {marks} with a grade of {grade}")
                    # subject[subject] = grade, marks
                    #maths = HD, 99
                    break
                # print(f"{subject} of marks: {marks} with a grade of {grade}")
        
        
        for detail0,info0 in Student.address.items():
            print(detail0, info0)
        print()
            
            

        
    
        

        
# Student 1 Results and Details
# print("Student 1 Results")
subjectA ={
    "Maths:": 34,
    "English:": 89,
    "French:": 77,
    "Chemistry:": 55,
}
#for subject0, marks0 in SubjectsA_dict.items():
    
    # print(subject0, marks0)
    
    
studentone = {
        "Student_ID:": "19191",
        "First Name:": "Jack",
        "Last Name:": "Sun",
        "Address:": "4 apple street",
        "State:": "VIC",
        "Postcode:": "3000",
}
# print("Student 1 Details")
#for details0, info0 in student1_dictionary.items():
    # print(details0, info0)
# Student 2 Results and Details
    # print("Student 2 Results")

subjectB = {
    "Physics:": 34,
    "Design:": 89,
    "Italian:": 77,
    "Programming:": 55,
}
#for subject1, marks1 in SubjectB_dict.items():
        # print( subject1, marks1)
        

studenttwo = {
    "Student_ID:": "19193",
    "First Name:": "Bob",
    "Last Name:": "Blue",
    "Address:": "4 Guava street",
    "State:": "NSW",
    "Postcode:": "2000",
}
#for details1, info1 in student2_dictionary.items():
    # print(details1, info1)

    
# for letter, number in GRADE_NUMBERING.items():
#     print(letter, number)


# def grade():
#     for topic, value in subject.items():
#      for letter, (high,low) in GRADE_NUMBERING.items():
#         if low <= value <= high and value <= 101:
#          print(f"{topic} score: {value} with a grade of {letter}")


def main():
    student1 = Student(19191, "Jack", "Sun", subjects= subjectA, address= studentone)
    # student1.grade()
    Student.display_info(student1)
    
    student2 = Student(19193,"Bob","Blue", subjects=subjectB, address= studenttwo)
    # student2.grade()
    Student.display_info(student2)
    
    student1.display_info()
    
main()
