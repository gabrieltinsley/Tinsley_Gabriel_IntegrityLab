# @author Gabriel Tinsley
# Hands-On Lab 2

# Part 2: Simulating the Low-Water-Mark Policy
# Define Integrity Levels
ACM = {
    "Alice": {"integrity": "High"},
    "Bob": {"integrity": "Low"},
    "File1": {"integrity": "Low"},
}

def low_water_mark_read(user, file):
    """Updates user integrity level to the minimum when reading."""
    user_level = ACM[user]["integrity"]
    file_level = ACM[file]["integrity"]
    # Update user's integrity to the lower level
    ACM[user]["integrity"] = min(user_level, file_level)
    print(f"{user} read {file}. Integrity now: {ACM[user]['integrity']}")
    
# Simulate Alice reading a low-integrity file
low_water_mark_read("Alice", "File1")  # Alice’s integrity should drop