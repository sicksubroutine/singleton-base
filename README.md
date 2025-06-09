# singleton-base

A minimal helper library providing a base class for implementing the singleton pattern in Python. It supports modern type hints and thread-safe instance creation.

## Installation

Install from PyPI with `pip`:

```bash
pip install singleton-base
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv pip install singleton-base
```

For development you can install the project in editable mode:

```bash
uv pip install -e .
```

## Usage

Subclass `SingletonBase` to make your class a singleton:

```python
from singleton_base import SingletonBase

class Config(SingletonBase):
    def __init__(self, value: int):
        self.value = value

# first call creates the instance
config = Config.get_instance(init=True, value=42)

# subsequent calls return the same instance
same_config = Config()
assert config is same_config
print(config.value)
```

`get_instance` ensures only one object exists. `reset_instance` removes the existing instance so a new one can be created.

## Testing

Run the full test suite with nox:

```bash
nox -s test_all_tests
```
