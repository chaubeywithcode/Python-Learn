# s = "hello world"  # String are immutable

# # s[0] = "R"  # You cannot do this

# a = len(s)
# print(a)

# Changing Case
# print(s.upper(), s)
# print(s.lower(), s)
# print(s.capitalize(), s)
# print(s.title(), s)

# text = "\nhello world "
# print(text.strip())     
# print(text.lstrip())    
# print(text.rstrip()) 

# text = "Python is fun"
# print(text.find("is"))  #Output: 7  Index of first occurence 
# print(text.replace("fun", "awesome"))

# text = "Apple,Banana,pineapple"
# print(text.split(","))

text = "Python123"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())
