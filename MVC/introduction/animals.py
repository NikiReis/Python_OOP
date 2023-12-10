class Animal:
    def walk(self):
        return "I'm walking as animal"
    
    def run(self):
        return "I'm running"
    
class Feline():
    def feline():
        return "I'm feline"

class Cat(Feline, Animal):
    def meow():
        return "I'm meowing"

class Dog(Animal):
    def bark():
        return "I'm barking"
    

"""x = Dog
# x.feline()
y = Cat
y.walk()"""
g = Cat()
print(f'{g.walk()}')