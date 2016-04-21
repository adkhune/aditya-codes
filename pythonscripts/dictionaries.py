import operator

def main():
    weekend = {"Sun": "Sunday", "Mon":"Monday"}
    items1 = {1: 7, 6: 3, 4:2 }
    print (weekend)
#    for i in items:
#        print (i) 
#        print (weekend[i])
        
#    for i,v in weekend.items():
#        print (": ".join((i,v)))

#    for i,v in items1.items():
#        print (": ".join((i,str(v))))
#    for i,v in items1.items():
#        print (": ".join((i,str(items1[i]))))

#    valueitems = items1.keys()
#    print(valueitems) 
#    valueitems.sort()
#    for i in valueitems:
#      print(":".join((str(i),items1[i])))

    for key in sorted(items1.items(), key=operator.itemgetter(0)):
        print ("{}: {}".format(key,items1[key]))

if __name__=="__main__": main()
