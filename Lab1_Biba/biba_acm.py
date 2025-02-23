# @author Gabriel Tinsley
# Hands-On Lab 2 CS331

# Part 1: Implementing the Biba Integrity Model

# Define user integrity levels
user_integrity = {
    "Alice" : "High",
    "Bob" : "Low",
    "Charlie" : "Low"
}

# Define ACM with Integrity Levels
ACM = {
    "Alice": {"File1": {"rights": ["read"]}},
    "Bob": {"File1": {"rights": ["write"]}},
    "Charlie": {"File2": {"rights": ["read"]}}
}

# Integrity level mapping for numeric comparison
integrity_levels = {"Low": 1, "High": 2}

def get_file_integrity(file):
    """Retrieve the integrity level of a file from any user entry."""
    for user in ACM:
        if file in ACM[user]:  # Find the first occurrence of the file
            return user_integrity.get(user, "Low")
    return "Low"  # Default to lowest level if file isn't explicitly listed

def check_access(user, file, action):
    """Checks if a user can access a file based on the Biba Model rules."""
    user_level_str = user_integrity.get(user, "Low") # Get user's integrity level
    file_level_str = get_file_integrity(file) # Get file's integrity level

    user_level = integrity_levels[user_level_str]
    file_level = integrity_levels[file_level_str]

    if action == "read" and user_level > file_level:
        print(f"Access Denied: {user} cannot read {file} (No Read Down)")
        return False
    elif action == "write" and user_level < file_level:
        print(f"Access Denied: {user} cannot write {file} (No Write Up)")
        return False
    else:
        print(f"Access Granted: {user} can {action} {file}")
        return True

# Testing Integrity Rules
check_access("Alice", "File2", "read") # Should be denied Test Case 1
check_access("Bob", "File1", "write")  # Should be denied Test Case 2
check_access("Alice", "File1", "read")  # Should be allowed Test Case 3