# let us right a code
# "the quick brown" in this sentence get all the vowels a, e, i, o, u
# and reverse its order, output the resultant string

def main():
    vowels = []
    outString = []
    print("Hi there")
    print("Give me an array of strings")
    str = input()
    reverse = len(str)
    print('you gave me \"'+ str + '\"')
    for i in str:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            vowels.append(i)
    reverse = len(vowels)
    print("reverse=",reverse)
    for j in range(0,len(str)):
        
        if str[j]=="a" or str[j]=="e" or str[j]=="i" or str[j]=="o" or str[j]=="u":
            reverse = reverse - 1
            outString.append(vowels[reverse])
        elif str[j] !=" ": outString.append(str[j])
        
    print(vowels)
    print(outString)

if __name__=="__main__": main()
