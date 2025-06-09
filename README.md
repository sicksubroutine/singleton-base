# singleton-base

A type-safe, thread-safe singleton base class for Python 3.9+. Very simple to use and test-friendly.

## Installation

### Using pip

```bash
pip install singleton-base
```

### Using Uv

```bash
uv add singleton-base
```

### Using Poetry

```bash
poetry add singleton-base
```

## Features

- Thread-safe: Multiple threads can safely create instances
- Type-safe: Full type hint support with modern typing on Python 3.11+
- Version adaptive: Automatically uses legacy implementation on Python < 3.11
- Test-friendly: Easy instance management for testing scenarios

## Usage

### Usage Example

Subclass using SingletonBase to make your class a singleton. All returned instances will now be the same object.

```python
from singleton_base import SingletonBase

class MySingleton(SingletonBase):
   def __init__(self, value: int):
       self.value = value

# Check if instance exists (initially False)
print(MySingleton.has_instance())  # False

# Create instance
singleton_instance = MySingleton(42)
print(MySingleton.has_instance())  # True

# Alternative creation method
MySingleton.reset_instance()  # Clear existing instance
singleton_instance2 = MySingleton.get_instance(init=True, value=42)
print(MySingleton.has_instance())  # True

# Get existing instance (safe - won't raise error)
if MySingleton.has_instance():
   singleton_instance3 = MySingleton.get_instance()

# This would raise RuntimeError if no instance exists:
# MySingleton.reset_instance()
# singleton_instance = MySingleton.get_instance()  # RuntimeError!

# Reset for testing or re-initialization
MySingleton.reset_instance()
print(MySingleton.has_instance())  # False

# Now you can create a new instance with different values
new_singleton = MySingleton(69)
print(new_singleton.value)  # 69
```

### Available Methods

| Method                             | Description                                                      |
| ---------------------------------- | ---------------------------------------------------------------- |
| get_instance(init=False, **kwargs) | Returns singleton instance. If init=True, creates it with kwargs |
| has_instance()                     | Returns True if singleton instance exists                        |
| reset_instance()                   | Destroys current instance, allows creating a new one             |

## Python Version Compatibility

Python 3.11+ uses modern implementation with more modern type hints.
Python 3.9-3.10 automatically falls back to legacy implementation.
Full test coverage across all supported versions.

## Testing

Run the full test suite with [nox](https://nox.thea.codes/):

```bash
nox -s test_all_tests
```

This command spins up test environments for every Python version configured in
``noxfile.py`` and executes all tests within each environment.
