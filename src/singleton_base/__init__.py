"""Singleton Base Class to make any other class a singleton with proper type hinting."""

__version__ = "1.0.3"


try:
    from typing import Self  # noqa: F401

    HAS_SELF = True
except Exception:
    HAS_SELF = False

if HAS_SELF:
    from .singleton_base_new import SingletonBase
else:
    from .singleton_base_legacy import SingletonBase


__all__ = ["SingletonBase", "__version__"]
