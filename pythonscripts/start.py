def main():
    print("Hare Krishna")
    sayhi()
    highscore =11
    score = 4
    msg = "I am screwed" if highscore > score else "but let us see"
    print(type(msg))
    
    if highscore > 11:
       print("high")
    elif highscore < 11:
       print("Low")
    else:
       print("I donno")		
    print(round(88/9))
    print("Let us play with list now")
    list1 = [1,4,2,9,7,0,9]
    print(list1[2:5:2])
    print('now let us see how for loop works')
    
#    for i in range(3,100): print(i,end=" ")
    list2 = []
    list2[:] = range(0,40)
#    print("list2=", list2)
    print('handling files anyone?')

def sayhi():
	print('jai shri krishna')    
    
    



if __name__=="__main__": main() 
