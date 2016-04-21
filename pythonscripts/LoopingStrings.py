#this code gives info about imp function such as split() how to convert a string
# into a list

def main():
    
    print("hare krishna")
    print("Give me a number")
    tp1 = input()
    print("you gave me", tp1)
    print("if you want the same string in reverse order, here you go:")
    for i in range(len(tp1)-1,-1,-1):
        print(tp1[i],end='')
    print("\n")
    for i in range(0,len(tp1)):
        print("the letter[%s] is %s" %(i,tp1[i]))
    print("Okay, converting into a list")
  
    words = tp1.split()
    print("you gave me",words)
        




if __name__=="__main__": main()
