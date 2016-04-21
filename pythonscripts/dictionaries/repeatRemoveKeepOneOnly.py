import pprint
def main():
    print('Hare Krishna')

    count = {}
    data = '122333441234'
    list1 = []
    print(data)
    for i in data:
        count.setdefault(i,0)
        count[i] = count[i]+1
    print(count)
    for i in range(0,len(data)):
        if i < len(data)-1 and data[i] == data[i+1]:
            #list1.append(data[i])
            #count[i]=0
            
            continue  
        else:
            list1.append(data[i])  
            #count[i] = 1
    print(list1)




if __name__=="__main__": main()
