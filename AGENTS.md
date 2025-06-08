# Contributor Guide for AI Agents

## Dev Environment Guidelines

### Claude Only

<antml:thinking_mode>interleaved</antml:thinking_mode><antml:max_thinking_length>16000</antml:max_thinking_length>

- Python Version and Typing: Assume Python 3.12 or higher is being used. Because of that we SHOULD use the latest typing features available in Python 3.12 and later. Never use `Optional`, `Union`, or `Dict, List, Tuple` from `typing` module. Instead, use the built-in types directly, e.g., `list`, `dict`, `tuple`, and use `|` for union types. This is not an exhaustive list, so be thoughtful about any potentially deprecated types you might use. If you are not sure about something, ask the user.
- Type Annotations: Use type annotations as often as possible. If a function has no return value, use `None` as the return type. If a function returns a value, use the appropriate type annotation but don't bend over backwards to make it perfect. If you are not sure about the type, use `Any` as a fallback but use this sparingly, see it as a failure and you should endeavor to avoid using `Any` as much as possible.
- Docstrings: Use docstrings for most (95%) public functions and classes. The docstring should describe the purpose of the function or class, its parameters, and its return value. Use the Google style for docstrings. Because of this it is highly preferred to not use comments in the code unless absolutely necessary. If you feel like you need to use a comment, consider if the code can be refactored to make it more readable instead.
- Imports: Use relative imports for everything (beyond the obvious imports for external packages) in this current package. Keep imports clean using `uv run isort src tests` and `uv run black src tests` to format the code in that order.
- Endeavor to use a TDD approach when writing new code. Write tests first, then write the code to make the tests pass and then refactor the code to make it cleaner and more readable.
- There is a `directory_structure.txt` file in the root of the repository that describes the directory structure of the project. Use this as a quick way to understand the project structure and where to place new files or modules.
- While projects might partially use Poetry, UV is generally the preferred tool for managing dependencies and virtual environments. It is taking me some time to get used to it, so please bear with me. If you are not sure about something, ask the user.
