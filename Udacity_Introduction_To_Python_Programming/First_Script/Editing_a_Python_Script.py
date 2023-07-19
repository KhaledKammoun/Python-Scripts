names = input("Enter names separated by commas : ").split(',')
assignments = [int(x) for x in input("Enter assignments separated by commas : ").split(',')]
grades = [int(x) for x in input("Enter names grades by commas : ").split(',') ]
for name, assignment, grade in zip(names, assignments, grades) :
    print("Hi {},\n\nThis is a reminder that you have {} assignments left to \nsubmit before you can graduate. You're current grade is {} and can increase \nto {} if you submit all assignments before the due date.\n\n".format(name,assignment,grade,assignment*2 + grade))