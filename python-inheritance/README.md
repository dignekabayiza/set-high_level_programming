# Python - Inheritance

This directory contains my work on Python inheritance, using the Python 3 interpreter.

## Files

- `0-lookup.py`: a function `lookup(obj)` that returns the list of available attributes and methods of an object.
- `2-is_same_class.py`: a function `is_same_class(obj, a_class)` that returns True if the object is exactly an instance of the specified class.
- `3-is_kind_of_class.py`: a function `is_kind_of_class(obj, a_class)` that returns True if the object is an instance of, or inherits from, the specified class.
- `4-inherits_from.py`: a function `inherits_from(obj, a_class)` that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class.
- `5-base_geometry.py`: an empty class `BaseGeometry`.
- `6-base_geometry.py`: a class `BaseGeometry` with an `area()` method that raises an Exception because it is not implemented.
- `7-base_geometry.py`: a class `BaseGeometry` with `area()` and an `integer_validator(name, value)` method that checks a value is an integer greater than 0.
- `8-rectangle.py`: a class `Rectangle` that inherits from `BaseGeometry` and validates a private width and height.
- `9-rectangle.py`: a class `Rectangle` that inherits from `BaseGeometry`, implements `area()` and prints as `[Rectangle] <width>/<height>`.
- `10-square.py`: a class `Square` that inherits from `Rectangle`, with a private validated size and an `area()` method.
- `11-square.py`: a class `Square` that inherits from `Rectangle`, implements `area()` and prints as `[Square] <width>/<height>`.
- `100-my_int.py`: a class `MyInt` that inherits from `int` and has the `==` and `!=` operators inverted.
