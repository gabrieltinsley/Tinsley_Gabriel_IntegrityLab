# @author Gabriel Tinsley
# Hands-On Lab 2

# Part 2: Simulating the Low-Water-Mark Policy
# Define Integrity Levels
ACM = {
    "Alice": {"integrity": "High"},
    "Bob": {"integrity": "Low"},
    "File1": {"integrity": "Low"},
}
# Maps integrity levels
integrity_levels = { "Low": 1, "High": 2}

def low_water_mark_read(user, file):
    """Updates user integrity level to the minimum when reading."""
    user_level_str = ACM.get(user, {}).get("integrity", "Low") # gets user integrity level
    file_level_str = ACM.get(file, {}).get("integrity", "Low") # gets file integrity level
    
    user_level = integrity_levels[user_level_str]
    file_level = integrity_levels[file_level_str]
    # Update user's integrity to the lower level
    ACM[user]["integrity"] = min(user_level, file_level)
    if ACM[user]["integrity"] == 1:
        ACM[user]["integrity"] = "Low"
    print(f"{user} read {file}. Integrity now: {ACM[user]['integrity']}")
    
def low_water_mark_write(user, file):
    """Denies write access if the users integrity level is lower than the files."""
    user_level_str = ACM.get(user, {}).get("integrity", "Low")
    file_level_str = ACM.get(file, {}).get("integrity", "Low")
    
    user_level = integrity_levels[user_level_str]
    file_level = integrity_levels[file_level_str]

    if user_level <= file_level:
        print(f"Write access denied: {user} (Integrity: {user_level_str}) cannot modify {file} (Integrity: {file_level_str})")
    else:
        print(f"Write access granted: {user} modified {file}.")

    
# Simulate Alice reading a low-integrity file
low_water_mark_read("Alice", "File1")  # Alice’s integrity should drop
low_water_mark_write("Alice", "File1") # Should be denied after Alice's integrity drops