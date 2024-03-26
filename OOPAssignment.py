class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hey, my name is {self.name}. I am {self.age} years old {self.gender}.")

# Create an instance of the Person class
person1 = Person("Valentine", 27, "female")

# Call the introduce method to display the person's information
person1.introduce()
