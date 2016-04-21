def main():
    list = [32,70,-1,0,66,14,30,31,90]
    print("numbers=",selectionSort(list))

def selectionSort(numbers):
#    minIndex = 0
#    min = numbers[0]
    for j in range(0,len(numbers)-1):
        minIndex = j
#        min = numbers[minIndex]
        for i in range(j+1,len(numbers)):
#            min = numbers[j+1]
            if numbers[minIndex] > numbers[i]:
                minIndex = i
#                min = numbers[minIndex]
        tmp = numbers[minIndex]
        numbers[minIndex] = numbers[j]
        numbers[j]=tmp
    return numbers



if __name__=="__main__": main()
