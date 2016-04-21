def main():
    list = [34,30,25,32,83,23,19]
    print("minimum number is=",min(list))
    print(len(list))
def min(numbers):
    min = numbers[0]
    for i in range(1,len(numbers)):
        print(i)
        if numbers[i] < min:
            min = numbers[i]
    return min








if __name__=="__main__": main()

