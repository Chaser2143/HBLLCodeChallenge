import time

def reverse_string(forward_string:str):
    '''Takes an input string and returns the string in reverse order'''
    if(type(forward_string) != str):
        raise Exception("Please input a string")
    reversed_string = ""
    for i in range(len(forward_string)-1, -1, -1): #Access the string like an array, and iterate backwards through it
        reversed_string += forward_string[i] #Add each char onto the new string
    # print(reversed_string)
    return reversed_string

def largest_num(num1:int, num2:int, num3:int):
    '''Takes 3 integers and returns the largest int found'''
    if((type(num1) != int) or (type(num2) != int) or (type(num3) != int)):
        raise Exception("Please input 3 valid integers")
    max_num = num1 #We could reduce space here without this variable, but it improves readability
    if num2 > max_num: #If the second number is bigger, set it as the max
        max_num = num2
    if num3 > max_num: #If the third number is bigger, set it as the max
        max_num = num3
    return max_num

def get_factorial(n:int):
    '''Returns the factorial of the inputted number'''
    if n<0:
        raise Exception("Please give a number at or above 0 as valid input")
    if n<=1: #Base Case
        return 1
    else:
        return n * get_factorial(n-1) #Recursive Case
    
def fib_helper(n:int, cache:dict):
    '''Returns the nth term in the fibonacci sequence'''
    if n<=0:
        raise Exception("Please input a number greater than or equal to 1 as input")
    if n<=2: #Base Case
        return 1
    else: #Recursive Case - Fibonacci number comes from prior 2 numbers added
        if cache.get(n-1) != None: #Is it already in the cache?
            n1 = cache.get(n-1) #If so, access it
        else:
            n1 = fib_helper(n-1, cache) #If not, calculate it and add it to the cache
            cache.update({n-1:n1})
        if cache.get(n-2) != None:
            n2 = cache.get(n-2)
        else:
            n2 = fib_helper(n-2, cache)
            cache.update({n-2:n2})
        return n1 + n2

def get_fibonacci(n:int):
    '''Holds dict as a cache to speed up fibonacci helper function'''
    cache = {}
    return fib_helper(n, cache)

def fibonacci_plain(n:int):
    '''Plain Fibonacci Sequence Calc, Gives nth term, no Cache'''
    if(n <=2): #Base Case
        return 1
    else: #Recursive Case - Fibonacci number comes from prior 2 numbers added
        return fibonacci_plain(n-1) + fibonacci_plain(n-2)

if __name__ == "__main__":
    print(reverse_string("st"))
    print(largest_num(5,7,3))
    print(get_factorial(12))
    t1 = time.time()
    print(get_fibonacci(100))
    t2 = time.time()
    print(fibonacci_plain(30))
    t3 = time.time()

    print(f"Time with Cache = {t2 -t1}")
    print(f"Time without Cache = {t3 -t2}")