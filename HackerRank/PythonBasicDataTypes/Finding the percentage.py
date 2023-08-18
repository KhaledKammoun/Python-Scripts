from statistics import mean 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average_score = mean(student_marks.get(query_name, [0.0]))
    print("{:.2f}".format(average_score))
