from threading import RLock
from typing import ClassVar, TypeVar, Union


class SingletonMeta(type):
    """Metaclass that enforces the singleton pattern."""

    _lock: ClassVar[RLock] = RLock()

    def __call__(cls, *args, **kwargs):
        """
        Return the singleton instance of the class.

        If the instance does not yet exist, it is created using the provided
        arguments. Uses a lock to ensure thread safety.

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
        """
        Return the singleton instance. If the instance does not yet exist, it is created using the provided
        arguments. Uses a lock to ensure thread safety.

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
        """
        Return ``True`` if the singleton instance has been initialized.

        Returns:
            bool: ``True`` if the instance exists, ``False`` otherwise.
        """
        return cls._instance is not None

    @classmethod
    def reset_instance(cls) -> None:
        """
        Reset the singleton instance to allow re-initialization.

        Uses a lock to ensure thread safety.
        """
        with cls._lock:
            cls._instance = None
