def validate_password(password):
    has_uppercase = password.lower() != password
    if not has_uppercase:
        return "Password should contain at least one uppercase letter."
    return "Password Validation Success"

# Example usage
password = input("Enter your password: ")
result = validate_password(password)
print(result)


