# Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts,
# and once for a list of grades. Use this input to create lists for names, assignments, and grades.

number_students = 3
names = []  # get and process input for a list of names
assignments = []  # get and process input for a list of the number of assignments
grades = []  # get and process input for a list of grades

for i in range(number_students):
    names.append(input(f"Student name {i+1}: "))
    assignments.append(
        int(float(input(f"Student {names[i]} number of assignments left: ")))
    )
    grades.append(float(input(f"Student {names[i]} grade until now: ")))

## message string to be used for each student
## HINT: use .format() with this string in your for loop
for i in range(number_students):
    message = f"\nHi {names[i]},\nThis is a reminder that you have {assignments[i]} assignments left to \n\
    submit before you can graduate. Your current grade is {grades[i]} and can increase \n\
    to {grades[i]+2*assignments[i]} if you submit all assignments before the due date.\n\n"
    print(message)

# Alternative solution

# names = input("Enter names separated by commas: ").title().split(",")
# assignments = input("Enter assignment counts separated by commas: ").split(",")
# grades = input("Enter grades separated by commas: ").split(",")

# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"

# for name, assignment, grade in zip(names, assignments, grades):
#    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
