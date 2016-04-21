import pprint
def main():
    print('Hare Krishna')
    found = False
    count = {}
    allnums = []
    iteration =1
    #data = '1222333441234'
    data = '00110'
    print(data)
    for i in data:
        count.setdefault(i,0)
        #count[i] = count[i]+1
    print(count)
    while iteration < 4:
        list1 = []
        for i in range(0,len(data)):
            if i < len(data)-1 and data[i] == data[i+1] and count[data[i]] == 0 and not found:
                #list1.append(data[i])
                #count[i]=0
                count[data[i]] = 1
                found = True
                continue  
            else:
                list1.append(data[i])  
                #count[i] = 1
        print(list1)
        allnums.append(''.join(list1))
        print(allnums)
        found = False
        iteration = iteration + 1




if __name__=="__main__": main()
