# Question 1
I have a scenario below where I need to find the best data structure.

Scenario: You have two very large lists of product IDs from two different suppliers. You need to find out which product IDs are present in both lists so you know which products you can source from either supplier. The order of the final list does not matter.

def find_common_elements(list1, list2):
    """Find the common elements between two lists.    This function should take two lists and return a new list containing    only the elements that are present in both input lists. The final    list can be in any order.    Parameters    ----------    list1 : list        The first list of elements.    list2 : list        The second list of elements.    Returns    -------    list        A list of elements common to both list1 and list2.    """
    pass

# Question 1 AI Response
For this scenario, the absolute best tool for the job is a **Hash Set** (or simply a `set` in Python).

### Why a Set?

When dealing with "very large lists," efficiency is everything. If you used a nested loop (comparing every item in List A to every item in List B), your time complexity would be , which is incredibly slow for large datasets.

By using a set, we leverage **hash tables**, which allow for:

* ** average time complexity:** We traverse each list once.
* **Constant time  lookups:** Checking if an item exists in a set is nearly instantaneous, regardless of how large the set is.
* **Automatic deduplication:** If a supplier accidentally listed the same ID twice, the set handles it for you.

---

### The Implementation

Python makes this particularly elegant because the `set` object has a built-in method for finding commonalities called `intersection`.

```python
def find_common_elements(list1, list2):
    """
    Finds common elements using a set intersection for O(n) efficiency.
    """
    # Convert the first list to a set
    # This takes O(n) time
    set1 = set(list1)
    
    # Convert the second list to a set
    # This takes O(m) time
    set2 = set(list2)
    
    # Find the intersection
    # This takes O(min(len(set1), len(set2))) time
    common_set = set1.intersection(set2)
    
    # Return as a list as requested
    return list(common_set)

```

### A More "Pythonic" Shortcut

If you want to keep the code concise, you can use the `&` operator, which performs the intersection automatically:

```python
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

```

### Performance Comparison

| Approach | Time Complexity | Performance on 1M Items |
| --- | --- | --- |
| **Nested Loops** |  | Hours (or worse) |
| **Sorting both lists** |  | Seconds |
| **Hash Set (The Winner)** |  | Milliseconds |

> **Note:** The only "cost" of using a set is memory. Since you are storing the IDs in a new data structure, it requires  space. Given that modern servers have plenty of RAM, this is almost always a trade-off worth making for the massive speed boost.

Would you like me to show you how to handle this if the data is so large that it doesn't fit into your computer's RAM?

# Question 2
I have a scenario below where I need to find the best data structure

Scenario: Your application loads a list of user profiles from a database. Each user has a unique username, an age, and an email address. You frequently need to look up a user's complete profile by their username. Performance is critical.

def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.    Parameters    ----------    users : list of dict        A list of dictionaries, where each dictionary represents a user        and has 'name', 'age', and 'email' keys. It is recommended to        convert this list into a more efficient data structure for lookups.    name : str        The name of the user to find.    Returns    -------    dict or None        The dictionary of the found user, or None if no user is found.    """
    pass

# Question 2 AI Response
To optimize for performance where lookup speed is the top priority, you should transform that list into a **Hash Map** (commonly implemented as a `dict` in Python).

---

## The Recommendation: Hash Map

While your input is a `list`, searching through it using a loop results in **linear time complexity**, or . This means if you have 1 million users, you might have to check all 1 million entries just to find one person.

By converting the list to a dictionary where the `username` is the **key**, you achieve **constant time complexity**, or .

### Performance Comparison

| Operation | List (Current) | Hash Map (Recommended) |
| --- | --- | --- |
| **Lookup Time** |  | **** |
| **Search Logic** | Scans every item | Jumps directly to the memory address |
| **Scalability** | Slows down as data grows | Speed remains constant |

---

## Implementation

To make this work, you first perform a one-time conversion of the list into a dictionary. This is a common pattern when "indexing" data for fast access.

```python
def find_user_by_name(users, name):
    # 1. Convert the list to a Hash Map (Dictionary) 
    # This 'indexing' step happens once, usually when the app loads.
    user_index = {user['name']: user for user in users}
    
    # 2. Perform the critical lookup
    # This is O(1) performance.
    return user_index.get(name)

```

### Why this is the "Best" Choice:

1. **Direct Mapping:** Since usernames are unique, they serve as the perfect "Key."
2. **Memory vs. Speed:** While a dictionary uses slightly more memory than a list, the trade-off is worth it for the near-instantaneous lookup speed.
3. **Simplicity:** Python’s built-in `dict` is highly optimized in C, making it faster than any custom search algorithm you might write for a list.

---

> **Note:** If the usernames were not unique, you would instead use a **Hash Map of Lists**, where each key points to a list of users with that name. However, since your scenario guarantees uniqueness, a standard Hash Map is ideal.

Would you like to see how to implement this using a **Class** to keep the index "warm" in memory so you don't have to rebuild it every time you search?

# Question 3
I have a scenario below where I need to find the best data structure

Scenario: You are given a list of integers representing sensor readings. You need to produce a report that contains only the even-numbered readings, and they must be presented in the exact same order they were received.

def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    The order of the numbers in the output list must be the same as the
    order of the even numbers in the input list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    list of int
        A new list containing only the even integers from the input list.
    """
    pass
# Question 3 AI Response
In this scenario, the best data structure is a **Dynamic Array** (simply a `list` in Python).

While the previous problem required a Hash Map for fast lookups, this task is about **filtering and preserving sequence**. A Dynamic Array is ideal because it maintains the relative order of elements and allows for efficient, sequential processing.

---

## Why a Dynamic Array?

### 1. Sequential Order

The primary requirement is to keep the "exact same order." Arrays and Lists are ordered by default (indexed), whereas structures like Sets or standard Hash Maps are not designed for maintaining sequence.

### 2. Time Complexity

To filter the list, you must inspect every single reading once.

* **Time:** , where  is the number of sensor readings. You cannot skip readings because any one of them could be even.
* **Space:** , where  is the number of even readings found.

### 3. Memory Efficiency

Since sensor data can be voluminous, a list is memory-efficient because it stores the integers contiguously without the overhead of "keys" or "pointers" required by dictionaries or linked lists.

---

## Implementation

The most "Pythonic" and efficient way to handle this is a **List Comprehension**. It is faster than a standard `for` loop because it is optimized at the bytecode level.

```python
def get_list_of_even_numbers(numbers):
    # This filters the list while maintaining the original sequence
    return [num for num in numbers if num % 2 == 0]

```

### How the logic works:

1. **Iterate:** It walks through the `numbers` list from index 0 to .
2. **Evaluate:** The modulo operator (`% 2 == 0`) checks if the number is even.
3. **Append:** If true, it adds the number to the new list, naturally preserving the original order.

---

## Alternative: Generator Expressions

If your list of sensor readings is massive (e.g., millions of entries) and you only need to process them one by one rather than storing them all in memory, you could use a **Generator**:

```python
def get_even_numbers_generator(numbers):
    return (num for num in numbers if num % 2 == 0)

```

* **Benefit:** Uses  extra space because it yields one number at a time.

Would you like to see how to handle this if you needed to remove the odd numbers "in-place" without creating a new list?