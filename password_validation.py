class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def validate_length(self):
        if len(self.password) < 12 or len(self.password) > 20:
            return "Password length should be between 12 and 20 characters."
        return None

    def validate_uppercase(self):
        if not any(char.isupper() for char in self.password):
            return "Password should contain at least one uppercase letter."
        return None

    def validate_lowercase(self):
        if not any(char.islower() for char in self.password):
            return "Password should contain at least one lowercase letter."
        return None

    def validate_number(self):
        if not any(char.isdigit() for char in self.password):
            return "Password should contain at least one digit."
        return None

    def validate_special_character(self):
        special_characters = "!@#$%^&*()_+=-[]{};':\"|,.<>/?"
        if not any(char in special_characters for char in self.password):
            return "Password should contain at least one special character."
        return None

    def validate_password(self):
        validations = [
            self.validate_length(),
            self.validate_uppercase(),
            self.validate_lowercase(),
            self.validate_number(),
            self.validate_special_character()
        ]

        print(validations)
        errors = [validation for validation in validations if validation is not None]

        if errors:
            return "\n".join(errors)
        return "Password Validation Success"


class ExtendedPasswordValidator(PasswordValidator):
    def validate_password(self):
        result = super().validate_password()
        if result == "Password Validation Success":
            return result

        missing_criteria = []
        if self.validate_length():
            missing_criteria.append("Length should be more than 12 and should not exceed beyond 20.")
        if self.validate_uppercase():
            missing_criteria.append("Should have at least one uppercase character.")
        if self.validate_lowercase():
            missing_criteria.append("Should have at least one lowercase character.")
        if self.validate_number():
            missing_criteria.append("Should have at least one number.")
        if self.validate_special_character():
            missing_criteria.append("Should have at least one special character.")

        return "\n".join(missing_criteria)


password = input("Enter your password: ")
validator = ExtendedPasswordValidator(password)
result = validator.validate_password()
print(result)
