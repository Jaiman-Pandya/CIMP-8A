class Employee:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number


    def display_info(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, first_name, last_name, id_number, monthly_salary):
        super().__init__(first_name, last_name, id_number)
        self.monthly_salary = monthly_salary

    def display_info(self):
        return "{:<10} {:<15} {:<15} {:<15}".format(self.id_number, self.first_name, self.last_name,'Full-Time')
        # return f"{self.id_number}   {self.first_name}   {self.last_name}    Full-Time"
        # return f"{self.first_name} {self.last_name} I.D.# {self.id_number}\nEmployee Type: Full-Time"

class PartTimeFaculty(Employee):
    def __init__(self, first_name, last_name, id_number, credit_units):
        super().__init__(first_name, last_name, id_number)
        self.credit_units = credit_units

    def display_info(self):
        # return f"{self.id_number}     {self.first_name}     {self.last_name}     PT Faculty"
        return "{:<10} {:<15} {:<15} {:<15}".format(self.id_number, self.first_name, self.last_name,'PT Faculty')

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, id_number, hourly_rate, hours_worked):
        super().__init__(first_name, last_name, id_number)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def display_info(self):
        return "{:<10} {:<15} {:<15} {:<15}".format(self.id_number, self.first_name, self.last_name,'Hourly')

        # return f"{self.id_number}   {self.first_name}   {self.last_name}    Hourly"

def main():
    employees = []

    try:
        with open("payroll.txt", "r") as file:
            lines = file.readlines()

        # print("Data loaded from payroll.txt:")
        for line in lines:
            parts = line.strip().split('\t')
            id_number = parts[0]
            first_name = parts[1]
            last_name = parts[2]
            employee_type = parts[3]

            if employee_type == "Full-Time":
                monthly_salary = float(parts[4])
                employee = SalaryEmployee(first_name, last_name, id_number, monthly_salary)
            elif employee_type == "Hourly":
                hourly_rate = float(parts[4])
                hours_worked = float(parts[5])
                employee = HourlyEmployee(first_name, last_name, id_number, hourly_rate, hours_worked)
            elif employee_type == "PT Faculty":
                credit_units = float(parts[4])
                employee = PartTimeFaculty(first_name, last_name, id_number, credit_units)
            else:
                print(f"Unknown employee type: {employee_type}")
                continue

            employees.append(employee)
            # print(line.strip())

    except FileNotFoundError:
        print("payroll.txt not found. Starting with an empty list.")

    print("\nWelcome to the Saddleback College Employee Payroll System.")
    while True:

        print("\nMenu:")
        print("(1) List All Employees")
        print("(2) Add a New Employee")
        print("(3) Remove an Existing Employee")
        print("(4) Display Info on an Employee")
        print("(5) Calculate Monthly Payroll")
        print("(6) Save Database")
        print("(7) Exit\n")

        print("Choose an option: ")

        choice = input()

        if choice == '1':
            print("Listing All Employees...\n")
            print("{:<10} {:<15} {:<15} {:<15}".format("I.D.#", "First Name", "Last Name", "Employee Type"))
            print("{:<10} {:<15} {:<15} {:<15}".format("-----", "----------", "---------", "-------------"))
            # I.D.#      First Name      Last Name       Employee Type
            # -----      ----------           ---------            -------------
            # 12345      John                 Adams                Full-Time
            # I.D.#      First Name      Last Name       Employee Type
            # -----      ----------      ---------       -------------
            # 12345      asad                 ali                  Full-Time
            # I.D.#      First Name      Last Name       Employee Type
            # -----      ----------      ---------       -------------
            # 12345      John            Adams           Full-Time
            # 12221      Andrew          Jackson         Hourly
            # 13332      Abraham         Lincoln         PT Faculty
            # 14563      John            Kennedy         Full-Time
            # 17894      Ronald          Reagan          Full-Time
            # 56791      Jane            Smith           PT Faculty
            seen_ids = set()

            for emp in employees:
                if emp.id_number not in seen_ids:
                    print(emp.display_info())
                    seen_ids.add(emp.id_number)

        elif choice == '2':
            print("Adding a New Employee...\n")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last  Name: ")
            id_number = input("Enter Employee 5-Digit I.D.#: ")
            print("Enter their job type:\nf - Full-Time\nh - Hourly\np - Part-Time Faculty")
            print('Choose an option: ',end='')
            job_type = input()


            if job_type == 'f':
                print("Enter their monthly salary: ")
                monthly_salary = float(input())
                employee = SalaryEmployee(first_name, last_name, id_number, monthly_salary)
            elif job_type == 'h':
                # print()
                hourly_rate = float(input("Enter their hourly rate: "))
                print("Enter the number of hours they worked (in 1 month): ")
                hours_worked = float(input())
                employee = HourlyEmployee(first_name, last_name, id_number, hourly_rate, hours_worked)
            elif job_type == 'p':
                print("Enter the number of units they teach: ")
                credit_units = float(input())
                employee = PartTimeFaculty(first_name, last_name, id_number, credit_units)

            employees.append(employee)
            print(f"Successfully added {first_name} {last_name}")

        elif choice == '3':
            print("Removing an Employee...\n")
            # print()
            first_name = input("Enter First Name: ")
            # print()
            last_name = input("Enter Last  Name: ")
            print("Enter Employee 5-Digit I.D.#: ")
            id_number = input()

            for emp in employees:
                if emp.first_name == first_name and emp.last_name == last_name and emp.id_number == id_number:
                    employees.remove(emp)
                    print(f"Successfully removed {first_name} {last_name}")
                    break

        elif choice == '4':
            print("Displaying Info on an Employee...\n")
            print("Enter First Name: ",end="")
            first_name = input()
            print("Enter Last  Name: ")
            last_name = input()

            for emp in employees:
                if emp.first_name == first_name and emp.last_name == last_name:
                    print("Employee found:\n")
                    print(emp.first_name+" "+emp.last_name+" - I.D.# "+emp.id_number)
                    if isinstance(emp, SalaryEmployee):
                        print("Employee Type: "+"Full-Time")
                        # print(f"Check Amount: ${emp.monthly_salary:.2f}")
                    elif isinstance(emp, PartTimeFaculty):
                        print("Employee Type: "+"PT Faculty")
                        # print(f"Check Amount: ${emp.credit_units * 1000:.2f}")
                    elif isinstance(emp, HourlyEmployee):
                        print("Employee Type: "+"Hourly")
                        # print(f"Check Amount: ${emp.hourly_rate * emp.hours_worked:.2f}")
                        # print("Employee Type: "+emp.__class__.__name__)

                    break

        elif choice == '5':
            print("Calculating Monthly Payroll...\n")
            for emp in employees:
                print(emp.first_name+" "+emp.last_name+" - "+"I.D.# "+emp.id_number)


                if isinstance(emp, SalaryEmployee):
                    print("Employee Type: "+"Full-Time")
                    print(f"Check Amount: ${emp.monthly_salary:.2f}")
                elif isinstance(emp, PartTimeFaculty):
                    print("Employee Type: "+"PT Faculty")
                    print(f"Check Amount: ${emp.credit_units * 3:.2f}")
                elif isinstance(emp, HourlyEmployee):
                    print("Employee Type: "+"Hourly")
                    print(f"Check Amount: ${emp.hourly_rate * emp.hours_worked:.2f}")
                print()

        elif choice == '6':
            try:
                with open("payroll.txt", "w") as file:
                    for emp in employees:
                        if isinstance(emp, SalaryEmployee):
                            file.write(f"SalaryEmployee,{emp.first_name},{emp.last_name},{emp.id_number},{emp.monthly_salary}\n")
                        elif isinstance(emp, PartTimeFaculty):
                            file.write(f"PartTimeFaculty,{emp.first_name},{emp.last_name},{emp.id_number},{emp.credit_units}\n")
                        elif isinstance(emp, HourlyEmployee):
                            file.write(f"HourlyEmployee,{emp.first_name},{emp.last_name},{emp.id_number},{emp.hourly_rate},{emp.hours_worked}\n")

                print("SUCCESS! payroll.txt is saved.")
            except Exception as e:
                print("Error saving the database:", str(e))

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    try:
        main()
    except:
        pass