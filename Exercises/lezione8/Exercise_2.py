#Exercise 2: Implementing Static Methods

#Create a class MathOperations with a static method add that takes two numbers and returns their sum, 
#and another static method multiply that takes two numbers and returns their product.

class MathOperations:

    @staticmethod
    def add(a: float, b:float):

        return a + b
    
    @staticmethod
    def multiply(a: float, b:float):

        return a * b
    
print()

somma: MathOperations = MathOperations()
moltiplicazione: MathOperations = MathOperations()

print(somma.add(a=2, b=2.5))

print(moltiplicazione.multiply(a=2, b=2.5))