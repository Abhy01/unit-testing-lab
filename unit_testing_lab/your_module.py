# your_module.py

def safe_divide(a: float, b: float) -> float:
    """Divides a by b. Returns 'inf' if b is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')


def string_analyzer(text: str) -> dict:
    """Analyzes a string and returns a dictionary of character counts."""
    return {
        'lowercase': sum(1 for c in text if c.islower()),
        'uppercase': sum(1 for c in text if c.isupper()),
        'digits': sum(1 for c in text if c.isdigit()),
        'spaces': text.count(' ')
    }
