class Animal:   #Parent class (superclass)
    location = "Japan"

    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now.....")

class Dog(Animal): #This is how inheritance is done in Python
    def speak(self):
        super().speak()  # We are using the speak function of the parent class
        print("Woof!")


d = Dog("Tomy")
d.speak()
print(d.location)

# a = Animal("dog")
# a.speak()