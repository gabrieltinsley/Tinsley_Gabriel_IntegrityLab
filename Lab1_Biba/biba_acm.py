# @author Gabriel Tinsley
# Hands-On Lab 2 CS331

# Part 1: Implementing the Biba Integrity Model

# Define ACM with Integrity Levels
ACM = {
    "Alice": {"File1": {"rights": ["read"], "integrity": "High"}},
    "Bob": {"File1": {"rights": ["write"], "integrity": "Low"}},
    "Jack": {"File2": {"rights": ["read"], "integrity": "Low"}},
    "Jill": {"File2": {"rights": ["write"], "integrity": "High"}},
}

def check_access(user, file, action):
    """Checks if a user can access a file based on the Biba Model rules."""
    user_level = ACM.get(user, {}).get(file, {}).get("integrity", "Low")
    file_level = ACM.get(user, {}).get(file, {}).get("integrity", "Low")

    if action == "read" and user_level < file_level:
        print(f"Access Denied: {user} cannot read {file} (No Read Down)")
        return False
    elif action == "write" and user_level > file_level:
        print(f"Access Denied: {user} cannot write {file} (No Write Up)")
        return False
    print(f"Access Granted: {user} can {action} {file}")
    return True

# Testing Integrity Rules
check_access("Alice", "File1", "read")  # Should be allowed
check_access("Bob", "File1", "write")  # Should be denied
check_access("Jill", "File2", "read") # Should be denied
check_access("Jack", "File2", "write") # Should be allowed
