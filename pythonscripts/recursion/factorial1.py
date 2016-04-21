import pandas
import timeit
def main():
    print("find of a factorial of n: n!")
    n = 6
    timeit
    print("fctorial of {} is {}".format(n,factorial(n)))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return  n * factorial(n-1)
    


if __name__=="__main__": main()
