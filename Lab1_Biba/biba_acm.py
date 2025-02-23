# @author Gabriel Tinsley
# Hands-On Lab 2 CS331

# Part 1: Implementing the Biba Integrity Model

# Define ACM with Integrity Levels
ACM = {
    "Alice": {"File1": {"rights": ["read"], "integrity": "High"}},
    "Bob": {"File1": {"rights": ["write"], "integrity": "Low"}},
}

# Integrity level mapping
integrity_levels = {"Low": 1, "High": 2}

# Checks if a user can access a file based on Biba Model rules
def check_access(user, file, action):
    user_level_str = ACM.get(user, {}).get(file, {}).get("integrity", "Low")
    file_level_str = next((ACM[u][file]["integrity"] for u in ACM if file in ACM[u]), "Low")
    
    user_level = integrity_levels[user_level_str]
    file_level = integrity_levels[file_level_str]

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
check_access("Bob", "File1", "write")   # Should be denied

