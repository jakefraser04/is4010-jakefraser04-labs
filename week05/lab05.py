users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def calculate_average_age(users: List[Dict[str, Any]]) -> float:
    """
    Calculate the average age of users.

    Filters out non-integer ages. Returns 0.0 if no valid data is found
    to maintain compatibility with existing test suites.

    Parameters
    ----------
    users : List[Dict[str, Any]]
        A list of user dictionaries.

    Returns
    -------
    float
        The average age, or 0.0 if no valid ages were processed.
    """
    valid_ages = [u["age"] for u in users if type(u.get("age")) is int]

    if not valid_ages:
        logger.warning("No valid user ages found. Returning 0.0 per requirements.")
        return 0.0

    avg = sum(valid_ages) / len(valid_ages)
    logger.info(f"Successfully calculated average age: {avg:.2f}")
    return avg

def get_active_user_emails(users: List[Dict[str, Any]]) -> List[str]:
    """
    Retrieve emails for active users.

    Logs a warning if an active user is missing an email address.

    Parameters
    ----------
    users : List[Dict[str, Any]]
        A list of user dictionaries.

    Returns
    -------
    List[str]
        A list of valid email strings.
    """
    active_emails = []
    
    for user in users:
        # Check if user is active AND has a truthy email value
        if user.get("is_active") is True:
            email = user.get("email")
            if email:
                active_emails.append(email)
            else:
                username = user.get("name", "Unknown User")
                logger.warning(f"Active user '{username}' is missing an email address.")
                
    return active_emails

if __name__ == "__main__":
    # Your mock data for local testing
    users_data = [
        {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
        {"name": "bob", "age": 25, "is_active": False},
        {"name": "charlie", "age": 35, "is_active": True},
        {"name": "david", "age": "unknown", "is_active": False}
    ]

    avg_age = calculate_average_age(users_data)
    emails = get_active_user_emails(users_data)

    print(f"\n--- Results ---")
    print(f"Average Age: {avg_age:.2f}")
    print(f"Emails: {emails}")