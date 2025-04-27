age = int(input("Enter your age: "))

if(age>18):
    print("you can drive")
elif(age==18):
    print("Lets schedule an interview")
elif(age==0):
    print("Hey you are just born")
else:
    print("Sorry you cannot drive")

print("End of program")