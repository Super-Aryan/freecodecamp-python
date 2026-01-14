# Basic Hash Table Implementation

This project implements a simple hash table in Python. It was created as part of an introductory Python assignment and is intended to demonstrate understanding of basic data structures and object-oriented programming.

---

## Overview

The hash table supports:
- Adding key-value pairs
- Looking up values by key
- Removing keys

Keys are hashed using a simple sum-of-ASCII approach, and collisions are handled by storing multiple keys in a nested dictionary at the same hashed value.

---

## Usage Example

```python
ht = HashTable()
ht.add("apple", 10)
ht.add("banana", 20)
print(ht.lookup("banana"))  # Output: 20
ht.remove("apple")
print(ht.lookup("apple"))   # Output: None
Notes
This implementation is intentionally basic and created to satisfy course requirements.
It is not intended for production use.
The hash function is simple and may result in collisions; collision handling is done with nested dictionaries.
The project focuses on practicing Python syntax, OOP, and data structure fundamentals.
