# String formatting

template = "Dear {}, You are awesome. Take this {}$ bag"
a ="John"
a1 = 10000
b = "jack"
b1 = 1000
c = "marie"
c1 = 300

s1 = template.format(a,a1)
print(s1)
s2 = template.format(b,b1)
print(s2)
s3 = template.format(c,c1)
print(s3)