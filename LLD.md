## Classes and Methods

### **Class Definition and Initialization**

- **Classes** are the blueprint for creating objects in Python.

```python
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1  # Instance variable
        self.attribute2 = attribute2

# Creating an object
obj = MyClass("value1", "value2")
```

### **Instance Variables and Methods**

- **Instance variables** are specific to each object.
- **Instance methods** operate on instance variables.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Example usage
p = Person("Alice", 25)
print(p.greet())  # Output: Hello, my name is Alice and I am 25 years old.
```

### **Class Variables and Class Methods**

- **Class variables** are shared among all instances of a class.
- **Class methods** operate on class variables and are denoted with `@classmethod`.

```python
class Counter:
    count = 0  # Class variable

    @classmethod
    def increment(cls):
        cls.count += 1

# Example usage
Counter.increment()
print(Counter.count)  # Output: 1
```

### **Static Methods**

- **Static methods** do not operate on class or instance variables. They are utility functions within a class.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example usage
print(MathUtils.add(5, 3))  # Output: 8
```

## OOP Concepts

### **Inheritance**

- Use inheritance to create a hierarchy of classes.

```python
class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"

# Example usage
dog = Dog()
print(dog.speak())  # Output: Woof!
```

### **Encapsulation**

- Use **private variables** to restrict access to attributes.
- Prefix variables with `_` (protected) or `__` (private).

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance

# Example usage
account = BankAccount(100)
print(account.get_balance())  # Output: 100
```

### **Polymorphism**

- Same interface but different implementations.

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow!
```

### **Abstraction**

- Use abstract classes to define methods that must be implemented in derived classes.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50
```

## Some Syntax Bits

### **Method Overloading (Default Arguments)**

- Python doesn't support true method overloading, but you can simulate it using default arguments.

```python
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

# Example usage
math = Math()
print(math.add(5))        # Output: 5
print(math.add(5, 3))     # Output: 8
print(math.add(5, 3, 2))  # Output: 10
```

### **Method Overriding**

- Redefine a method from the parent class in the child class.

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

# Example usage
child = Child()
print(child.greet())  # Output: Hello from Child
```

## Design Principles