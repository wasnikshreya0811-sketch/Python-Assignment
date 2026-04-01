import os
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
class Result(Student):
    def __init__(self, name, marks):
        super().__init__(name, marks)
        self.total = 0
        self.percentage = 0
        self.grade = ""
    # function to calculate total, percentage and grade
    def calculate(self):
        self.total = sum(self.marks)
        self.percentage = self.total / len(self.marks)
        # assigning grade
        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 80:
            self.grade = "A"
        elif self.percentage >= 70:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        elif self.percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "F"
    # function to create marksheet file
    def create_marksheet(self, folder_name):
        file_name = os.path.join(folder_name, self.name + "_marksheet.txt")
        f = open(file_name, "w")
        f.write("********************************\n")
        f.write("        STUDENT MARKSHEET       \n")
        f.write("********************************\n\n")
        f.write("Name : " + self.name + "\n\n")
        # printing marks of each subject
        i = 1
        for mark in self.marks:
            f.write("Subject " + str(i) + " : " + str(mark) + "\n")
            i += 1
        f.write("\n")
        f.write("Total : " + str(self.total) + "\n")
        f.write("Percentage : " + str(round(self.percentage, 2)) + "%\n")
        f.write("Grade : " + self.grade + "\n")
        f.write("\n********************************\n")
        f.close()
def main():
    input_file = "data.txt"
    folder = "marksheets"
    # create folder if not present
    if not os.path.exists(folder):
        os.mkdir(folder)
    # check if file exists
    if not os.path.exists(input_file):
        print("data.txt file not found")
        return
    count = 0
    file = open(input_file, "r")
    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        try:
            name = parts[0]
            marks = []
            # converting marks into integer
            for m in parts[1:]:
                marks.append(int(m))
            s = Result(name, marks)
            s.calculate()
            s.create_marksheet(folder)
            count += 1
        except:
            print("Error in line:", line)
    file.close()
    print(count, "marksheets created successfully!")
# calling main function
main()