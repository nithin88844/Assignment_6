 
# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.




class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"Dog details \nName : {self.name} \nAge : {self.age} \nCoat color : {self.coat_color}"

    
    def description(self):
        print(f"Dog discription \nName : {self.name} \nAge : {self.age}")
        
    def get_info(self):
        print(f"coat color : {self.coat_color}")


class JackRussellTerrier(Dog):
    def height(self):
        height = input("enter dog height : ")
        print("height :",height)

    def color(self):
        color = input("enter dog color : ")
        print("color :",color)

class Bulldog(Dog):
    def weight(self):
        weight = input("enter dog weight : ")
        print("weight :",weight)

    def vaccine_count(self):
        count = int(input("enter the no. of vaccine count :"))
        print(f"vaccine count : {count}")
        
        





# dog_obj = Dog(input("Enter dog name : "),int(input("Enter dog age : ")),input("Enter dog coat color : "))
# dog_obj.description()
# dog_obj.get_info()

obj = JackRussellTerrier(input("Enter dog name : "),int(input("Enter dog age : ")),input("Enter dog coat color : "))
obj.description()
obj.height()

