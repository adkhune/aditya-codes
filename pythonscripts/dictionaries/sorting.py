import operator

def main():
    print('Let us see how to sort in dictionaries')
    dict1 = {'aa':1, 'pp':4, 'cc':2, 'tt':3}
    print('this is our dict1=', dict1)
    sorted_dict1 = sorted(dict1.items(), key=operator.itemgetter(1))
    print('after sorting it acc to values=',sorted_dict1)
    sorted_dict2 = sorted(dict1.items(), key=operator.itemgetter(0))
    print('sorting it acc to keys=',sorted_dict2)
    print('these were list of tuples\nif we want dictionary then..')
    print(dict(sorted_dict1))
    print(dict(sorted_dict2))





if __name__=="__main__": main()
