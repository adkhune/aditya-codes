def main():
    print("Hare Krishna!")
    print("Let us do merge sorting !!")
#    print(3//2)
#    print("range=",[range(0,6)])
    list = [4,2,3,1,8,9,0,4]
    tp = []
    for p in range(0, 9):
        tp.append(p)
    print(tp)
    print(mergeSort(list, 0, len(list)-1))


def mergeSort(list, start, end):
    middle = (start + end)//2
#    print("middle=",middle)
    if start < end:
        print("call mergesort Left")
        mergeSort(list,start,middle)
        print("call mergesort Right")
        mergeSort(list, middle+1, end)
        merge(list, start, middle, end)

def merge(list, start, middle, end):
    n1 = middle - start + 1
    n2 = end - middle
    left = []
    right = []
    print("called merge sort now")
    for i in range(0, n1):
        left.insert(i, list[start + i])
    for j in range(0, n2):
        right.insert(j, list[middle + 1 + j])
    l = 0
    m = 0
    for k in range(start, end-1):
        if left[l] <= right[m]:
            list.insert(k, left[l])
            l = l + 1
        else:
            list.insert(k, right[m])
            m = m + 1
    return list



if __name__=="__main__": main()
