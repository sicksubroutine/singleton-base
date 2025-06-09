from threading import RLock
from typing import ClassVar, Self


class SingletonMeta(type):
    """Metaclass that enforces the singleton pattern."""

    _lock: ClassVar[RLock] = RLock()

    def __call__(cls, *args, **kwargs) -> object:
        """Create or return the singleton instance.

        Args:
            *args: Positional arguments for ``cls.__init__``.
            **kwargs: Keyword arguments for ``cls.__init__``.

        Returns:
            object: The singleton instance.
        """
        if not hasattr(cls, "_instance") or cls._instance is None:
            with cls._lock:
                if not hasattr(cls, "_instance") or cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class SingletonBase(metaclass=SingletonMeta):
    """
    A base class for singleton classes

    Provides multiple helper methods to manage the singleton instance:
    - `get_instance`: Returns the singleton instance, initializing it if necessary.
    - `has_instance`: Checks if the singleton instance has been initialized.
    - `reset_instance`: Resets the singleton instance to allow re-initialization.
    """

    _instance: ClassVar[Self | None] = None

    @classmethod
    def get_instance(cls, init: bool = False, **kwargs) -> Self:
        """Return the singleton instance.

        Args:
            init: Whether to initialize the instance if it does not yet exist.
            **kwargs: Arguments passed to ``cls`` when creating the instance.

        Returns:
            Self: The singleton instance of the class.

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
