# @author Gabriel Tinsley
# Hands-On Lab 2

# Part 3: Implementing the Ring Policy
# ACM with integrity levels
ACM = {
    "Alice": {"integrity": "High"},
    "Bob": {"integrity": "Low"},
    "File1": {"integrity": "Medium"}
}

# Maps integrity levels
integrity_levels = { "Low": 1, "Medium": 2, "High": 3}

def ring_policy(user, file, action):
    """Implements Ring Policy: All can read, only high-integrity can modify."""
    user_level_str = ACM.get(user, {}).get("integrity", "Low") # gets user integrity level
    file_level_str = ACM.get(file, {}).get("integrity", "Low") # gets file integrity level
    
    user_level = integrity_levels[user_level_str]
    file_level = integrity_levels[file_level_str]
    
    if action == "read":
        print(f"Access Granted: {user} can read {file}")
    elif action == "write" and user_level >= file_level:
        print(f"Access Granted: {user} can write to {file}")
    else:
        print(f"Access Denied: {user} cannot modify {file}")

# Alice can modify File1, Bob cannot
ring_policy("Alice", "File1", "write") # Alice can write to File1
ring_policy("Bob", "File1", "read") # Bob can read File1
ring_policy("Bob", "File1", "write")  # Should be denied