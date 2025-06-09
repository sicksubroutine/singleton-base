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

### Basic Singleton

Subclass SingletonBase to make your class a singleton. All instances will be the same object.

```python
from singleton_base import SingletonBase

class MySingleton(SingletonBase):
    def __init__(self, value: int):
        self.value = value

# Usage
singleton_instance = MySingleton(42)
# Also Valid
singleton_instance2 = MySingleton.get_instance(init=True, value=42)

# If you do this get_instance without init=True and an instance doesn't exist, it will give an RuntimeError:
singleton_instance2 = MySingleton.get_instance(value=42)

# Assuming the instance was correctly corrected and you are in another context:
singleton_instance3 = MySingleton.get_instance()
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
