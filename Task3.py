import re

def assess_password_strength(password):
    # Initialize strength score
    strength_score = 0

    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    # Increment strength score based on criteria met
    if length_criteria:
        strength_score += 1
    if uppercase_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if number_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 1

    # Determine password strength
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Medium"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

# Example usage
password = input("Enter a password to assess its strength: ")
strength, feedback = assess_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")
