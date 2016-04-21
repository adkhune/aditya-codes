# digit string manipulation example
# 122399404427 if this is input then output
#12399404427 12239404427 12239940427
# and give me the largest number
import re
from collections import Counter

def main():
    str = '1223999404427'
    print("you gave me", str)
    numRegex = re.compile(r'(\d)\1*')
    num = numRegex.findall(str)

    c = Counter(re.findall(r'\d',str))
    print(c)



if __name__=="__main__": main()
