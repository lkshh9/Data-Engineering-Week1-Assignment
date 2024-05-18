if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
#No need of 'if' even, if we know student exists and no need to test it.
    print(format(sum(student_marks[query_name])/len(student_marks[query_name]),'.2f'))