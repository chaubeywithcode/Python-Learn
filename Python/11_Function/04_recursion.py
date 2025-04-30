'''
fibonacci

0 1 1 2 3 5 8 13
0 1 2 3 4 5 6  7

fib(0) = 0
fib(1) = 1
fib(n) = fib(n-2) + fib(n-1)

'''

def fib(n):
    if(n == 0 or n == 1):
        return n
    else:
        return fib(n-2)+ fib(n-1)

#  0 1 1 2 3 5 8 13
#  0 1 2 3 4 5 6  7   
print(fib(6))

'''
4+5
2+3+3+4
0+1+1+  2+1+2+3+2
0+1+1+0+1+1+0+1+1+2+0+1
0+1+1+0+1+1+0+1+1+0+1+0+1


'''

'''
Factorial
4! = 1 * 2 * 3 * 4 = 24

'''
def factorial(n):
    if n == 1 or 0:
        return n
    
    else:
       return n* factorial(n-1) 

print(factorial(4))


