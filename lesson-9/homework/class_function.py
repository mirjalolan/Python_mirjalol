# 1. Circle Class
import math
from datetime import datetime

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
# circle = Circle(5)
# print(f"Area: {circle.area():.2f}")
# print(f"Perimeter: {circle.perimeter():.2f}")


# 2. Person Class
class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year
    
    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year
    
    def info(self):
        return f"{self.name} from {self.country}, age {self.age()}"

# Example usage:
# person = Person("Alice", "USA", 1990)
# print(person.info())


# 3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

# Example usage:
# calc = Calculator()
# print(calc.add(10, 5))
# print(calc.divide(10, 3))


# 4. Shape and Subclasses
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

# Example usage:
# square = Square(4)
# triangle = Triangle(3, 4, 5)
# print(f"Square area: {square.area()}")
# print(f"Triangle area: {triangle.area():.2f}")


# 5. Binary Search Tree Class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Example usage:
# bst = BinarySearchTree()
# bst.insert(50)
# bst.insert(30)
# bst.insert(70)
# print(bst.search(30))  # True
# print(bst.search(100)) # False


# 6. Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


# Example usage:
# stack = Stack()
# stack.push(1)
# stack.push(2)
# print(stack.pop())  # 2


# 7. Linked List Data Structure
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Example usage:
# ll = LinkedList()
# ll.insert(1)
# ll.insert(2)
# ll.insert(3)
# print(ll.display())  # [3, 2, 1]


# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]['quantity'] += quantity
        else:
            self.items[name] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, name, quantity=None):
        if name in self.items:
            if quantity is None or quantity >= self.items[name]['quantity']:
                del self.items[name]
            else:
                self.items[name]['quantity'] -= quantity
    
    def total_price(self):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total
    
    def display_cart(self):
        for name, details in self.items.items():
            print(f"{name}: ${details['price']} x {details['quantity']}")

# Example usage:
# cart = ShoppingCart()
# cart.add_item("Apple", 1.50, 3)
# cart.add_item("Banana", 0.75, 2)
# print(f"Total: ${cart.total_price()}")


# 9. Stack with Display
class StackWithDisplay:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
    
    def display(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.copy()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

# Example usage:
# stack = StackWithDisplay()
# stack.push("A")
# stack.push("B")
# print(stack.display())  # ['A', 'B']


# 10. Queue Data Structure
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

# Example usage:
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# print(queue.dequeue())  # 1


# 11. Bank Class
class BankAccount:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Invalid amount or insufficient funds"
    
    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, name, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, name, initial_balance)
            return f"Account created for {name}"
        return "Account already exists"
    
    def get_account(self, account_number):
        return self.accounts.get(account_number, "Account not found")
    
    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            sender = self.accounts[from_account]
            receiver = self.accounts[to_account]
            
            if sender.balance >= amount and amount > 0:
                sender.balance -= amount
                receiver.balance += amount
                return f"Transferred ${amount} from {from_account} to {to_account}"
            return "Invalid amount or insufficient funds"
        return "One or both accounts not found"

# Example usage:
# bank = Bank()
# bank.create_account("123", "John")
# bank.create_account("456", "Jane")
# account = bank.get_account("123")
# print(account.deposit(100))
# print(bank.transfer("123", "456", 50))
