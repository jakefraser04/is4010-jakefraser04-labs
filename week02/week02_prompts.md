# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

### Problem 1 Prompt
**Context:** This function is supposed to calculate the sum of all **even** numbers in a list, but it contains a logical error.

**Buggy code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
```

**Persona:** You are a senior python developer.
**Task:** Your task is to debug this code so it runs and calculates as necessary.
**Format:** Please return a documented code block explaining all code and specifically the changes you made.

---

### AI Response

Hello! As a Senior Python Developer, I can certainly help you patch this up.

The issue lies in the conditional logic within your `for` loop. You were checking for a remainder of **1** (which identifies *odd* numbers), rather than a remainder of **0** (which identifies *even* numbers).

Here is the corrected code with detailed documentation explaining the logic and the specific fix.

#### Corrected Implementation

```python
def sum_of_evens(numbers):
    """
    Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers to be processed.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    # Initialize the accumulator variable
    total = 0
    
    # Iterate through every number in the input list
    for num in numbers:
        # BUG FIX: changed 'num % 2 == 1' to 'num % 2 == 0'
        # The modulo operator (%) returns the remainder of the division.
        # If a number divided by 2 has a remainder of 0, it is even.
        if num % 2 == 0:
            total += num
            
    return total

# Example Usage:
# sample_list = [1, 2, 3, 4, 5, 6]
# result = sum_of_evens(sample_list)
# print(f"The sum is: {result}")  # Output will be 12 (2 + 4 + 6)
```

#### Senior Dev Tip: The "Pythonic" Approach

While the `for` loop above is perfectly readable and correct, experienced Python developers often prefer using the built-in `sum()` function combined with a generator expression. This reduces the function to a single, efficient line of code.

Here is how I would write this in a production environment:

```python
def sum_of_evens_efficient(numbers):
    """
    Calculate the sum of all even numbers using a generator expression.
    
    This method is more concise and generally considered more 'Pythonic'.
    It iterates over 'numbers', filters for evenness, and sums them instantly.
    """
    return sum(num for num in numbers if num % 2 == 0)
```

## Problem 2: Refactoring

### Problem 2 Prompt
**Context:** This function works correctly, but it's written in a confusing, non-Pythonic way.

**Code:**
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users    who are 18 or older.    Parameters    ----------    users : list of dict        List of user dictionaries with 'name' and 'age' keys.    Returns    -------    list of str        Names of users who are 18 or older.    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```

**Persona:** You are a senior python developer.
**Task:** Refactor this code to be more clear, concise, and idiomatic.
**Format:** Return results like the previous answer, in markdown fashion.

---

### AI Response

Hello! I'd be happy to refactor this for you.

The original code suffers from a common "C-style" anti-pattern in Python: iterating using indices (`range(len(users))`) when it isn't necessary. In Python, we can iterate directly over the elements of a list.

Below are two refactored versions: one that improves the loop readability, and one that is the "idiomatic" (standard) Python approach using a list comprehension.

#### Refactor 1: The List Comprehension (Recommended)

This is the most "Pythonic" way to handle this task. It combines the filtering (checking age) and the mapping (extracting names) into a single, readable line.

```python
def get_names_of_adults(users):
    """
    Return a list of names of users who are 18 or older.
    
    This implementation uses a list comprehension for conciseness and speed.
    """
    return [user['name'] for user in users if user['age'] >= 18]
```

#### Refactor 2: The Explicit Loop (Readable)

If you find list comprehensions difficult to read or if the logic were more complex, this is the correct way to write the standard loop. Note that we iterate over `user` directly, removing the need for `users[i]`.

```python
def get_names_of_adults_explicit(users):
    """
    Return a list of names of users who are 18 or older.
    """
    results = []
    for user in users:
        # Directly access the dictionary; no index 'i' needed
        if user['age'] >= 18:
            results.append(user['name'])
    return results
```

## Problem 3: Documentation

### Problem 3 Prompt
**Context:** This function works correctly but has no documentation.

**Undocumented code:**
```python
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**Persona:** You are a senior python developer.
**Task:** Write a professional NumPy-style docstring for this function.
**Format:** Like the previous answer, in markdown fashion.

---

### AI Response

Hello! Clear documentation is critical for maintainable code. Since you asked for the **NumPy style**, I will ensure the docstring includes the standard sections: `Parameters`, `Returns`, and `Raises`.

Here is the fully documented function:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle given its length and width.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be a positive number.
    width : float or int
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float or int
        The calculated area (length multiplied by width).

    Raises
    ------
    ValueError
        If either `length` or `width` is less than or equal to zero.
    
    Examples
    --------
    >>> calculate_area(5, 10)
    50
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```
