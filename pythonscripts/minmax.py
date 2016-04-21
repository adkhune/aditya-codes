def main():
    list = [3,5,6,32,56,32,2,3]
    min, max = minmax(list)
    print("min={} and max={}".format(min,max))


def minmax(numbers):
    min=numbers[0]
    max=numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
        if numbers[i] > max:
            max = numbers[i]

    return min, max

if __name__=="__main__": main()
