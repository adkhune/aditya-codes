# Regular expression practice
import re

def main():
    str = '''
Aditya Khune 28,
Apurva Khune 24,
Dilip Khune 50,
Geeta Khune 42'''
    print(countPeople(str))
    print(onlyNames(str))
    print(NameAge(str))
    for i in NameAge(str): print(i) # ('Name', 'age')
    for i in NameAge(str): print(i[0] +" "+ i[1]) # Name age
    

def NameAge(str):
    NameAgeRegex = re.compile(r'(\w+)\s\w+\s(\d+)')
    NameAge = NameAgeRegex.findall(str)
    return NameAge

def onlyNames(str):
    namesRegex = re.compile(r'(\w+)\sKhune')
    names = namesRegex.findall(str)
    print("onlyNames=",names)
    return len(names)


def countPeople(str):
    namesRegex = re.compile(r'\w+\sKhune')
    names = namesRegex.findall(str)
    print("fullNames=",names)
    return len(names)


if __name__=="__main__":main()
