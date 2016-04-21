#create an integer array, which holds values from 0 to 3999 (inclusive).
#Each value must appear once and only once, no duplicates.

import random
def main():
    print('hi there')
    print('here is a random number', random.randint(0,9))
    print('use function now', rand(0,9))
    dict1 = {}
    list1 = []
    list2 = []
#    dict1.update({1:3})
#    for i in range(200):
    while len(list1) < 21:
        x = random.randint(0,20)
#        print(x)
        dict1.setdefault(x,0)
        dict1[x] = dict1[x] + 1
        if dict1[x] == 1:
            list1.append(x)
    print(dict1)
    print("\n")
    print(list1)
    while len(list2) < 21:
        y = random.randint(0,20)
        if y not in list2: list2.append(y) #
    print(list2)

    print(4 in dict1)# very simple way to find if number is present in a dictionary
def rand(x,y):
    return random.randint(x,y)

if __name__=="__main__":main()
