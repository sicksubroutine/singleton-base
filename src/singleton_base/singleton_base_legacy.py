"""Singleton Base Class to make any other class a singleton with proper type hinting."""

from threading import RLock
from typing import ClassVar, TypeVar, Union


class SingletonMeta(type):
    """Metaclass that enforces the singleton pattern."""

    _lock: ClassVar[RLock] = RLock()

    def __call__(cls, *args, **kwargs):
        """Return the singleton instance of the class.

        If the instance does not yet exist, it is created using the provided
        arguments.

        Args:
            *args: Positional arguments forwarded to the class constructor.
            **kwargs: Keyword arguments forwarded to the class constructor.

        Returns:
            The singleton instance.
        """
        if not hasattr(cls, "_instance") or cls._instance is None:
            with cls._lock:
                if not hasattr(cls, "_instance") or cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


T = TypeVar("T", bound="SingletonBase")


class SingletonBase(metaclass=SingletonMeta):
    """A base class for singleton classes with a typed get_instance method."""

    _instance: ClassVar[Union[T, None]] = None  # type: ignore[assignment]

    @classmethod
    def get_instance(cls: type[T], init: bool = False, **kwargs) -> T:
        """Return the singleton instance.

        Args:
            init: Whether to initialize the instance if it does not yet exist.
            **kwargs: Arguments passed to ``cls`` when creating the instance.

        Returns:
            T: The singleton instance of the class.

        Raises:
            RuntimeError: If ``init`` is ``False`` and the instance has not been initialized.
        """
        if cls._instance is None and not init:
            raise RuntimeError(f"Instance of {cls.__name__} is not initialized yet")
        elif cls._instance is None and init:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls(**kwargs)
        return cls._instance

    @classmethod
    def has_instance(cls) -> bool:
        """Return ``True`` if the singleton instance has been initialized.

        Returns:
            bool: ``True`` if the instance exists, ``False`` otherwise.
        """
        return cls._instance is not None

    @classmethod
    def reset_instance(cls) -> None:
        """Reset the singleton instance to allow re-initialization.

        Returns:
            None
        """
        with cls._lock:
            cls._instance = None


"""
if __name__ == "__main__":
    # example usage

    class ExampleClass(SingletonBase):
        '''A simple example class to demonstrate the singleton pattern.'''

        def __init__(self, value: int):
            self.value = value

        def __repr__(self):
            return f"ExampleClass(value={self.value})"

    a: ExampleClass = ExampleClass(1)
    b: ExampleClass = ExampleClass(2)
    print(a is b)  # True, same instance
    print(a)  # ExampleClass(value=1)
    print(b)  # ExampleClass(value=1), same instance with the same value since init was not called again

    singleton_instance = ExampleClass.get_instance()
    print(singleton_instance)  # ExampleClass(value=1)

    class ExampleClassWithArgs(SingletonBase):
        '''A simple example class to demonstrate the singleton pattern with arguments.'''

        def __init__(self, value: int):
            self.value = value

        def __repr__(self):
            return f"ExampleClassWithArgs(value={self.value})"

    a2 = ExampleClassWithArgs(6)
    b2 = ExampleClassWithArgs(2)
    print(a2) # ExampleClassWithArgs(value=6)
    print(b2) # ExampleClassWithArgs(value=6), same instance with the same value since init was not called again
    print(a2 is b2)  # True, same instance

    print(a == a2)

    singleton_instance = ExampleClassWithArgs.get_instance()
"""
