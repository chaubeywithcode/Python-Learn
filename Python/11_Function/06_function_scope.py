def sum(a,b):
    # a and b are local variables
    c = a + b
    z = 1 # It creates a local variable called z which is destroyed after this function return
    return c

z = 8 # z is a global variable
print(z)
print(sum(4,6))
print(z)