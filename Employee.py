class Employee:
    def __init__(self, name, ID_number, department, job_title):
        self.name = name
        self.ID_number = ID_number
        self.department = department
        self.job_title = job_title

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.ID_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print("-" * 30)  # Separator for readability


# Initialize Objects with given data
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Display data for each employee
print("Employee Data:\n" + "=" * 30)
employee1.display_info()
employee2.display_info()
employee3.display_info()
