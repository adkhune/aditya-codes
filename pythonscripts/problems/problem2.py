# You are given a int[] marks containing the grades you have received so
# far in a class. Each grade is between 0 and 10, inclusive. Assuming
# that you will receive a 10 on all future assignments, determine the
# minimum number of future assignments that are needed for you to
# receive a final grade of 10. You will receive a final grade of 10 if
# your average grade is 9.5 or higher.


def main():
    list_marks = []
    print("give me marks")
    marks = input()
    print("you gave me", marks)
    list_marks = marks.split()
    for i in range(len(list_marks)): list_marks[i] = int(list_marks[i])
    print("list_marks=", list_marks)
    print("more tests with score 10 needed =",need(list_marks))


def need(marks):
    avg = findAvg(marks)
    append = 0
    print("avg is", avg)
    if avg < 9.5:
        while avg < 9.5:
            marks.append(10)
            print("appended 10, now the numbers are", marks)
            avg = findAvg(marks)
            print("and the new avg is", avg)
            append = append+1
        return append
    elif avg >= 9.5:
        return 0

def findAvg(marks):
    sum = 0
    avg = 0.0
    for i in range(len(marks)):
        sum = sum + marks[i]
    avg = sum/len(marks)
    return round(avg,4)


if __name__=="__main__": main()
