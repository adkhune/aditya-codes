def main():
    list = [5,3,1,0,53,21,331,2,6,8,0]
    print(bubblesort(list))



def bubblesort(numbers):
    print("length=",len(numbers),"list[3]=",numbers[3])
    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                tmp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = tmp
            
   
    return numbers




if __name__=="__main__": main()
