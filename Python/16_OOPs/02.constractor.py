class Employee:
    
    def __init__ (self, salary, name , bond):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond

        

    def get_salary(self):   # Self is important here because self is a way to reference the object of the class witch is being created
        return self.salary
    
    def get_info(self):
        print(f"The nameof the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} year")

e = Employee(34000, "Anurag",4)

e.get_info()

