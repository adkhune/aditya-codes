def main():
    print("In this code let us read from a file and do somethin with it")
    print("--------------------------------------------------------------")        
    tuple1 = ()
    list1 = []
    dict1 = {}
    dict2 = {}
    list2 = []
     

    try:
        file = open("sample2_file.txt")
    except:
        print("file not found")
    else:
        for i in file:
            list1.append(i.split())
            print(i,end="")
        dict1 = dict(list1)
        print("                                                            ")
        print("dict1=",dict1)
        print("--------------------------------------------------------------")        
        dict2 = dict((v,k) for k,v in dict1.items())
        print("dict2=", dict2)





        file.close()
if __name__=="__main__": main()
