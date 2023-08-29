def my_enumerate(lessons, start = 0) : # start take a zero by default
    for lesson in lessons :
        yield start, lesson
        start += 1
for i,lesson in my_enumerate(['a','b','c'],5) :
    print("Lesson {} : {}".format(i, lesson))