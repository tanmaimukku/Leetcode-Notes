**RoadMap**

Classes - Methods, Attributes, Class Variables, Class Methods 2) OOPS concepts - Abstraction, Polymorphism, Encapsulation, Inheritance 3) super() method 4) Design Principles - SOLID, DRY, KISS, YAGNI 5) Design Patterns - Only important ones - Singleton, Factory Method, Builder, Strategy, Observer 6) Importants concepts/classes to know - Unique ID generation, Desgining Rate Limiter (Token bucket, fixed window), Caching (LRU, LFU), Queue management (Asynchronous Processing of Tasks, Desiognning notifications Systems using message queue/observer patterns), time based schedulers like crons jobs, load balancing algorithms, Data Paginiation and limtiing results, Search and Fileting, Acces contro and permissions, Handling concurrency and synchronization

**Important Questions to Practice:**

 1. **Pizza Shop Question**
 2. **Unix/linux File search question**
 3. **LRU Cache (Indirect uses too), with TTL**
 4. **LFU Cache**
 5. **Hotel Booking/Management System** 
 6. **<span style="font-family: -apple-system, system-ui, Segoe UI, Roboto, Helvetica Neue, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, sans-serif; color: rgb(51, 61, 66); font-size: 14px">elevator system in a building</span>**
 7. **<mark data-color="#ffe066" style="background-color: #ffe066; color: inherit">Parking Lot Design</mark>**
 8. **Load Balancer**
 9. **File Management System**
10. **URL shortner**
11. **Income Calculator**
12. **Hashtable**
13. **Amazon Locker System (Scalable storage locker)**
14. **Amazon Package Delivery System**
15. **Amazon Validation of a Purchase class**
16. **Design Calendar**
17. **Abstract Data structure that supports find/add/retrieve/delete etc.**
18. **Custom collection class - getRandome, add, retrieve etc.** 
19. **Find Connected id given list of id's (friends, their tastes etc.)**
20. **Historical search terms by frequency of search (Trie)**
21. **API Gateway**
22. **Games - Chess Game, Snake and Ladder, Wordle, Spell Bee, Sudoku etc.**
23. **Rate Limiter** 
24. **Common LLD Questions - Library, Vending Machine, Amazon Online shopping System, Movie ticket booking etc.** 
25. **Notification System LLD**
26. **Most frequent/vs least frequent in huge database - heap internals/Trie**
27. **Autocomplete - Trie**

# Classes and Methods

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

# OOP Concepts

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

# Design Principles

## SOLID Principles

1. **Single Responsibility Principle (SRP)**:

   - **Definition**: A class should have only one reason to change, meaning it should only have one job.

   - **Example**:

     ```python
     class Invoice:
         def __init__(self, items):
             self.items = items
     
         def calculate_total(self):
             return sum(self.items)
     
     class InvoicePrinter:
         def print_invoice(self, invoice):
             print(f"Invoice Total: {invoice.calculate_total()}")
     ```

     - **Why**: Separates the responsibilities of calculating and printing the invoice.

2. **Open/Closed Principle (OCP)**:

   - **Definition**: A class should be open for extension but closed for modification.

   - **Example**:

     ```python
     class Discount:
         def apply_discount(self, price):
             return price
     
     class PercentageDiscount(Discount):
         def __init__(self, percent):
             self.percent = percent
     
         def apply_discount(self, price):
             return price * (1 - self.percent / 100)
     ```

     - **Why**: New discount types can be added by extending the `Discount` class without modifying existing code.

3. **Liskov Substitution Principle (LSP)**:

   - **Definition**: Subtypes must be substitutable for their base types.

   - **Example**:

     ```python
     class Bird:
         def fly(self):
             pass
     
     class Sparrow(Bird):
         def fly(self):
             print("Sparrow flying")
     
     def make_bird_fly(bird):
         bird.fly()
     
     make_bird_fly(Sparrow())  # Works correctly
     ```

     - **Why**: Subclasses like `Sparrow` can replace `Bird` without breaking functionality.

4. **Interface Segregation Principle (ISP)**:

   - **Definition**: A class should not be forced to implement interfaces it does not use.

   - **Example**:

     ```python
     class Printer:
         def print(self):
             pass
     
     class Scanner:
         def scan(self):
             pass
     
     class AllInOneMachine(Printer, Scanner):
         def print(self):
             print("Printing...")
     
         def scan(self):
             print("Scanning...")
     ```

     - **Why**: The interfaces are split into `Printer` and `Scanner`, so classes only implement what they need.

5. **Dependency Inversion Principle (DIP)**:

   - **Definition**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

   - **Example**:

     ```python
     class Database:
         def save(self, data):
             pass
     
     class MySQLDatabase(Database):
         def save(self, data):
             print("Saving data to MySQL")
     
     class Application:
         def __init__(self, database: Database):
             self.database = database
     
         def store_data(self, data):
             self.database.save(data)
     
     app = Application(MySQLDatabase())
     app.store_data("Sample data")
     ```

     - **Why**: The `Application` class depends on the abstraction `Database`, not on the concrete implementation.

## DRY (Don’t Repeat Yourself)

- **Definition**: Avoid duplicating code by abstracting common functionality.

- **Example**:

  ```python
  def calculate_area(length, width):
      return length * width
  
  class Rectangle:
      def __init__(self, length, width):
          self.length = length
          self.width = width
  
      def area(self):
          return calculate_area(self.length, self.width)
  ```

## KISS (Keep It Simple, Stupid)

- **Definition**: Keep designs simple and avoid unnecessary complexity.

- **Example**:

  ```python
  def add(a, b):
      return a + b
  ```

  - Avoid overengineering a simple addition function.

## YAGNI (You Aren’t Gonna Need It)

- **Definition**: Don’t implement functionality until it’s actually required.

- **Example**:

  ```python
  class Feature:
      def useful_function(self):
          print("This is useful now.")
  ```

  - Avoid adding speculative methods or features "just in case" they are needed later.

# DESIGN PATTERNS (Only Important Ones)

## 1. Singleton Pattern

- **Purpose**: Ensures that a class has only one instance and provides a global access point to it.
- **Key Use Cases**: Configuration managers, database connections, logging systems.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

## 2. Factory Method Pattern

- **Purpose**: Creates objects without specifying the exact class. Lets subclasses decide which class to instantiate.
- **Key Use Cases**: When a method must return objects of different types based on conditions.

```python
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def notify(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def notify(self):
        print("Sending SMS Notification")

class NotificationFactory:
    @staticmethod
    def create_notification(type_):
        if type_ == "email":
            return EmailNotification()
        elif type_ == "sms":
            return SMSNotification()
        else:
            raise ValueError("Invalid notification type")

# Usage
factory = NotificationFactory()
notification = factory.create_notification("email")
notification.notify()  # Output: Sending Email Notification
```

## 3. Builder Pattern

- **Purpose**: Constructs complex objects step by step, separating construction logic from the representation.
- **Key Use Cases**: Building objects with multiple optional parameters.

```python
class House:
    def __init__(self):
        self.rooms = 0
        self.garage = False
        self.swimming_pool = False

    def __str__(self):
        return f"House with {self.rooms} rooms, Garage: {self.garage}, Pool: {self.swimming_pool}"

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_rooms(self, rooms):
        self.house.rooms = rooms
        return self

    def add_garage(self):
        self.house.garage = True
        return self

    def add_pool(self):
        self.house.swimming_pool = True
        return self

    def build(self):
        return self.house

# Usage
builder = HouseBuilder()
luxury_house = builder.set_rooms(4).add_garage().add_pool().build()
print(luxury_house)  # Output: House with 4 rooms, Garage: True, Pool: True
```

## 4. Strategy Pattern

- **Purpose**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime.
- **Key Use Cases**: Dynamic algorithm selection, e.g., different payment methods.

```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_expiry):
        self.card_number = card_number
        self.card_expiry = card_expiry

    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card ending in {self.card_number[-4:]}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paying ${amount} using PayPal account {self.email}")

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paying ${amount} using Bitcoin wallet {self.wallet_address}")

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_amount = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_amount += price

    def pay(self, payment_strategy: PaymentStrategy):
        payment_strategy.pay(self.total_amount)

# Create a shopping cart
cart = ShoppingCart()
cart.add_item("Book", 15)
cart.add_item("Pen", 5)

# Pay using different strategies
cart.pay(CreditCardPayment("1234-5678-9012-3456", "12/23"))
cart.pay(PayPalPayment("user@example.com"))
cart.pay(BitcoinPayment("1A2b3C4d5E6f7G8h9I0J"))
```

## 5. Observer Pattern

- **Purpose**: Defines a one-to-many dependency where multiple observers are notified of changes in the subject’s state.
- **Key Use Cases**: Event-driven systems, like GUIs or notifications.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(data)

from abc import ABC, abstractmethod

class Observer:
    @abstractmethod
    def update(self, data):
        pass

class EmailObserver(Observer):
    def update(self, data):
        print(f"Email Observer: Received data - {data}")

class SMSObserver(Observer):
    def update(self, data):
        print(f"SMS Observer: Received data - {data}")

# Usage
subject = Subject()
email_observer = EmailObserver()
sms_observer = SMSObserver()

subject.add_observer(email_observer)
subject.add_observer(sms_observer)

subject.notify_observers("System Update Available!")
# Output:
# Email Observer: Received data - System Update Available!
# SMS Observer: Received data - System Update Available!
```