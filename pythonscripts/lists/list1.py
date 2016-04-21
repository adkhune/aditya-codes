def main():
    print("hare krishna")
    list1 = []
    list2 = []
    for i in range(0,6):
        list1.insert(i, i)
    print(list1)
    for j in range(0,6):
        list2.insert(j,list1[j])
    print(list2)
    i = 2
    j = 2
    for t in range(0,6):
        if list1[t] == list2[t]:
            print("equal")



if __name__=="__main__" : main()
