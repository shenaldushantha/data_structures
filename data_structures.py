# data_structures.py

class Node:
    """Base node class for tree implementations."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation with basic operations."""
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a new value into the BST."""
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper method for recursive insertion."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def inorder_traversal(self):
        """Perform in-order traversal of the BST."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for recursive in-order traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

class HashTable:
    """Hash Table implementation with linear probing for collision resolution."""
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def _hash_function(self, key):
        """Simple hash function for string/integer keys."""
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        return key % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        if self.count >= self.size * 0.7:  # Resize if load factor > 0.7
            self._resize()
        
        index = self._hash_function(key)
        while self.table[index] is not None:
            # If key exists, update value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        
        self.table[index] = (key, value)
        self.count += 1
    
    def get(self, key):
        """Retrieve a value by key from the hash table."""
        index = self._hash_function(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        
        raise KeyError(f"Key '{key}' not found")
    
    def _resize(self):
        """Resize the hash table when load factor exceeds threshold."""
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        
        for item in old_table:
            if item:
                self.insert(item[0], item[1])

class Stack:
    """Stack implementation using a Python list."""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

class Queue:
    """Queue implementation using a Python list."""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the first item in the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Queue is empty")
    
    def peek(self):
        """Return the first item without removing it."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0