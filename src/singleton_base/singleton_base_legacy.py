"""Singleton Base Class to make any other class a singleton with proper type hinting."""

from threading import RLock
from typing import ClassVar, TypeVar, Union


class SingletonMeta(type):
    """
    A metaclass for creating singleton classes.
    This metaclass ensures that only one instance of the class exists.
    """

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
        """Returns the singleton instance of the class."""
        if cls._instance is None and not init:
            raise RuntimeError(f"Instance of {cls.__name__} is not initialized yet")
        elif cls._instance is None and init:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls(**kwargs)
        return cls._instance

    @classmethod
    def has_instance(cls) -> bool:
        """Check if the singleton instance has been initialized."""
        return cls._instance is not None

    @classmethod
    def reset_instance(cls) -> None:
        """Reset the singleton instance to allow re-initialization."""
        with cls._lock:
            cls._instance = None
