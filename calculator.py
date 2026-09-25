"""Basic calculator operations."""


def add(first, second):
    """Return the sum of two numbers."""
    return first + second


def subtract(first, second):
    """Return the difference between two numbers."""
    return first - second


def multiply(first, second):
    """Return the product of two numbers."""
    return first * second


class Calculator:
    """Provide basic calculator operations."""

    add = staticmethod(add)
    subtract = staticmethod(subtract)
    multiply = staticmethod(multiply)
