def main():
    print("                         **********                         ")        
    print("                         **********                         ")        
    print("                         **********                         ")        
    print('Hare Krishna, Let is study dictionarieds now.')
    print('These are the ways in which dictionary is declared as follows:')
    dict1 = dict(one=1,two=2)
    print("1. dict1 = dict(one=1,two=2)")
    print("--------------------------------------------------------------")
    dict2 = dict([('one',1),('two',2)])
    print("2. dict([(\'one\',1),(\'two\',2)])")
    print("--------------------------------------------------------------")
    dict3 = dict(one="Monday",two="Tuesday",three="Wednesday")
    print("3. dict(one=\"Monday\",two=\"Tuesday\",three=\"Wednesday\")")
    print("--------------------------------------------------------------")
    dict4 = {'one':1, 'two':2}
    print("4. dict3 = {\'one\':1, \'two\':2}")
    print("--------------------------------------------------------------")


    print(" for pair in dict1.items():\n print(pair)=")    
    for pair in dict1.items():
        print(pair)    
    print("--------------------------------------------------------------")
    print(" for key,value in dict1.items():\n print(key,value)=")    
    for key,value in dict1.items():
        print(key,value)    
    print("--------------------------------------------------------------")
    print(" for key,value in dict3.items():\n print(key,value)=")    
    for key,value in dict3.items():
        print(key,value)    
    print("--------------------------------------------------------------")
    print("                         **********                         ")        
    print("                         **********                         ")        
    print("                         **********                         ")        
if __name__=="__main__": main()
