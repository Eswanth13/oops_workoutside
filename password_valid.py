class Passwordvalidation:
    def __init__(self,password):
        self.password=password
    def length_validater(self):
        if len(self.password)<12 or len(self.password)>20:
            print('Length should be more than 12 and should not exceed beyond 20')
        else:
            return password
    def upper_validate(self):
        upper_password=self.password.lower() != self.password
        if not upper_password:
            return "Password should contain at least one uppercase letter."
        return password

