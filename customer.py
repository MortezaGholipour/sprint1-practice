class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"
