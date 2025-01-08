def validate_password(password):
    # Conditions for validation
    conditions = {
        "digit": any(char.isdigit() for char in password),
        "lowercase": any(char.islower() for char in password),
        "uppercase": any(char.isupper() for char in password),
        "special": any(not char.isalnum() for char in password),
    }

    # Check password length
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return

    # Check for missing elements
    missing_elements = [key for key, present in conditions.items() if not present]

    if missing_elements:
        for element in missing_elements:
            if element == "digit":
                print("Password is missing a digit.")
            elif element == "lowercase":
                print("Password is missing a lowercase letter.")
            elif element == "uppercase":
                print("Password is missing an uppercase letter.")
            elif element == "special":
                print("Password is missing a special character.")
    else:
        print("Password is valid!")

# Test the function
password = input("Enter a password to validate: ")
validate_password(password)
