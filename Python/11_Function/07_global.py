def sum(a, b):
    print("Hey I am summing")
    c = a + b
    global z
    z = 5 # This will refer to global z and not create a local variable
    return c

z = 3

print(sum(3,4))
print(z)