"""
Collection of code snippets, keywords, and dev memes for Dev Hero game.
"""

import random

# Python snippets
PYTHON_SNIPPETS = [
    "from pprint import pprint",
    "ValueError: invalid literal for int()",
    "try: except:",
    "lambda x: x * 2",
    "def __init__(self):",
    "import os, sys",
    "if __name__ == '__main__':",
    "raise NotImplementedError",
    "async def fetch_data():",
    "with open('file.txt') as f:",
    "list(map(lambda x: x**2, range(10)))",
    "[x for x in range(10) if x % 2 == 0]",
    "f'{name} is {age} years old'",
    "except Exception as e:",
    "yield from generator()",
]

# JavaScript snippets
JAVASCRIPT_SNIPPETS = [
    "const arrowFunction = () => {}",
    "console.log('Hello World')",
    "async function fetchData() {}",
    "const [a, b] = array",
    "obj?.property?.nested",
    "Array.from(new Set(arr))",
    "Promise.all(promises)",
    "const { name, age } = user",
    "arr.map(x => x * 2)",
    "`${variable} template`",
]

# Error messages that every dev hates
ERROR_MESSAGES = [
    "Merge conflict detected",
    "Unexpected token '<'",
    "NullPointerException",
    "404 Not Found",
    "500 Internal Server Error",
    "SyntaxError: unexpected EOF",
    "TypeError: Cannot read property",
    "ModuleNotFoundError: No module named",
    "IndentationError: expected an indented block",
    "ReferenceError: variable is not defined",
]

# Classic dev memes
DEV_MEMES = [
    "I have no idea why this works",
    "Works on my machine",
    "Rubber duck debugging",
    "It's not a bug, it's a feature",
    "Copy-paste from Stack Overflow",
    "Just ship it",
    "This should be quick",
    "I'll fix it later",
    "The code is self-documenting",
    "It works in production",
    "I tested it locally",
    "That's a hardware issue",
    "Works for me",
    "Can't reproduce",
    "It's a caching issue",
]

# Programming keywords
KEYWORDS = [
    "function",
    "variable",
    "algorithm",
    "recursion",
    "iteration",
    "polymorphism",
    "inheritance",
    "encapsulation",
    "abstraction",
    "asynchronous",
    "callback",
    "promise",
    "closure",
    "decorator",
    "generator",
    "iterator",
    "singleton",
    "factory",
    "observer",
    "middleware",
]

# All challenges combined
ALL_CHALLENGES = (
    PYTHON_SNIPPETS +
    JAVASCRIPT_SNIPPETS +
    ERROR_MESSAGES +
    DEV_MEMES +
    KEYWORDS
)


def get_random_challenge():
    """Return a random challenge from all available challenges."""
    return random.choice(ALL_CHALLENGES)


def get_challenges_by_category(category):
    """Get challenges by category.
    
    Args:
        category: One of 'python', 'javascript', 'errors', 'memes', 'keywords'
    
    Returns:
        List of challenges from the specified category
    """
    categories = {
        'python': PYTHON_SNIPPETS,
        'javascript': JAVASCRIPT_SNIPPETS,
        'errors': ERROR_MESSAGES,
        'memes': DEV_MEMES,
        'keywords': KEYWORDS,
    }
    return categories.get(category.lower(), ALL_CHALLENGES)

