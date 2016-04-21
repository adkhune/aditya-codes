import re
'''
Identifiers:

\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. = \.
. = any character, except a new line
\b the whitespace around words
\. a period

Modifiers:

{1,3} we're expecting 1-1 \d{1-3}
+ match one or more
? match 0 or 1
* match 0 and more
$ match end of a string
^ beginning of a string
| either or \d{1-3} | \w{5-6}
[] range or variance
{5} expecting "5" amount


ages = re.findall(r'\d{1,3}','examplestring)
names re.findall(r'')


'''


def main():
    file = open("file.txt")
    for i in file:
        patternMatch = re.search("in",i)
        if patternMatch:
            print("pattern={} {}".format(i,patternMatch.group))



if __name__=="__main__": main()
