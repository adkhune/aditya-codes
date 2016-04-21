import re
phoneNumber = re.compile(r'\d\d\d-\d\d\d')
mo = phoneNumber.findall('call me 970-481 tomorrow 759-483')
def main():
    print("Hi there", phoneNumber)
    print(mo)
 


if __name__=="__main__": main()
