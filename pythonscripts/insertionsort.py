def main():
    list = [2,5,0,6,7]
    print("sorted numbers=",insertionSort(list))

def insertionSort(numbers):
    for i in range(0,len(numbers)):
        current = numbers[i]
        j = i-1
        while numbers[j] > current and j>=0:
            numbers[j+1] = numbers[j]
            j=j-1            
        numbers[j+1] = current


    return numbers



if __name__=="__main__": main()
