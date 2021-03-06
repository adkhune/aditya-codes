def main():
    print("                         **********                         ")        
    print("                         **********                         ")        
    print("                         **********                         ")        
    print("In this code let us read from a file and do somethin with it")
    print("--------------------------------------------------------------")        
    tuple1 = ()
    list1 = []
    dict1 = {}
    list2 = []
     
    print("try:")
    print("    file = open(\"sample_file.txt\")")
    print("except:")
    print("    print(\"file not found\")")
    print("else:")
    print("    for line in file:")
    print("        print(line,end=\"\")")
    print("                                                            ")
    try:
        file = open("sample2_file.txt")
    except:
        print("file not found")
    else:
        for i in file:
            list1.append(i.split())
            print(i,end="")
        print("--------------------------------------------------------------")        
        print("-------let us read file into list1 and print-------")
        print("for i in file:")
        print("    list1.append(i.split())")
        print("    print(i,end=\"\")")
        print("                                                            ")
        print("list1=",list1)
        print("--------------------------------------------------------------")        
        print("-------now let us convert list1 into dict1 and print-------")
        print("dict1 = dict(list1)")        
        print("print(\"dict1=\",dict1)")
        dict1 = dict(list1)
        print("                                                            ")
        print("dict1=",dict1)
        print("--------------------------------------------------------------")        
        print("----------example of list comprehension as follows------------")
        print("list2 = [line.strip() for line in open(\"sample_file.txt\",'r')]")
        print("print(\"list2=\",list2)")
        list2 = [line.strip() for line in open("sample2_file.txt",'r')]
        print("                                                            ")
        print("list2=",list2)
        print("------.strip() is used get rid of \\n, in the end dont forget to do file.close()------")
        print("--------------------------------------------------------------")        
        print("                         **********                         ")        
        print("                         **********                         ")        
        print("                         **********                         ")        
        file.close()
if __name__=="__main__": main()
