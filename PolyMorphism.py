# What is Polymorphism in python?
 # In my definition polymorphism in python is a way of using general code to refer to objects that are in other codes.✌️

#Examples:
➡️ Function Polymorphism:
   #. According to my reasearch Function Polymorphism can be used in diffferent ways (1) is in Functions; Such as the len() this function allows us to get the length or how many words or items are in a list, dictionary,tuple.😍         
#Examples:
my_list = ["Apple", "Banana", "Cherry"]
length = len(my_list)
print(f"The length of the list is {length}.")
# If you run this code above you will be able to see the output of 3.

➡️ Class Polymorphism;
   # Using class/objects; When using Class/Objects it's easier to add more classes/objects into our classes
#Examples: 
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
  
#@nifemi_2011 Vscode Code
#@(c) Nifemi_2011 @2024
