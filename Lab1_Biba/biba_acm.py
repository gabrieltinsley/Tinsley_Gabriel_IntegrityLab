# @author Gabriel Tinsley
# Hands-On Lab 2 CS331

# Part 1: Implementing the Biba Integrity Model

# @author Gabriel Tinsley
# Hands-On Lab 2 CS331

# Part 1: Implementing the Biba Integrity Model

# Define ACM with Integrity Levels
ACM = {
    "Alice": {"File1": {"rights": ["read"], "integrity": "High"}},  # High Integrity
    "Bob": {"File1": {"rights": ["write"], "integrity": "Low"}},   # Low Integrity
    "Charlie": {"File2": {"rights": ["read"], "integrity": "Low"}}, # Low Integrity
}

# Integrity level mapping for numeric comparison
integrity_levels = {"Low": 1, "High": 2}

def get_file_integrity(file):
    """Retrieve the integrity level of a file from any user entry."""
    for user in ACM:
        if file in ACM[user]:  # Find the first occurrence of the file
            return ACM[user][file]["integrity"]
    return "Low"  # Default to lowest level if file isn't explicitly listed

def check_access(user, file, action):
    """Checks if a user can access a file based on the Biba Model rules."""
    user_level_str = ACM.get(user, {}).get(file, {}).get("integrity", "Low")
    file_level_str = get_file_integrity(file)

    user_level = integrity_levels[user_level_str]
    file_level = integrity_levels[file_level_str]

    if action == "read" and user_level < file_level:
        result = f"Access Denied: {user} cannot read {file} (No Read Down)"
    elif action == "write" and user_level > file_level:
        result = f"Access Denied: {user} cannot write {file} (No Write Up)"
    else:
        result = f"Access Granted: {user} can {action} {file}"
    
    print(result)
    return result

# Running test cases and writing results to a file
test_results = []
test_results.append("Test Case 1: High-Integrity Subject Reading a Low-Integrity Object")
test_results.append(check_access("Alice", "File2", "read"))  # Expect: Denied

test_results.append("\nTest Case 2: Low-Integrity Subject Writing to a High-Integrity Object")
test_results.append(check_access("Bob", "File1", "write"))  # Expect: Denied

# Write results to a file
with open("biba_test_results.txt", "w") as f:
    f.write("\n".join(test_results))

