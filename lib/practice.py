class User:
    def __init__(self, name):
        self.name = name


    def log_in(self):
        print("User.log_in() called.")
        self.logged_in = True


class Student(User):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def log_in(self):
        print(f"{self.name} has logged in! Grade = {self.grade}")
        super().log_in()
        self.in_class = True

Keith = Student("Keith", "B+")
Keith.log_in()