from Backend.company import Company
from Backend.employee import *
from Backend.items import *
from Backend.invoice import Invoice

class FrontendManager:
    def __init__(self):
        self.company = Company()
        self.payroll = self.company.payroll
        self.invoices = list()
    
    def menu(self):
        self.options = [
            "Add Volunteer",
            "Add Hourly-based employee",
            "Add Salary-based employee",
            "Add Commsion-salary-based employee",
            "Add Invoice",
            "Display Inforamtion",
            "Exit"
            ]
        self.menu = [f"{number}- {option}" for number, option in zip(range(1, len(self.options)+1), self.options)]
        return '\n'.join(self.menu)

    
    def add_volunteer(self):
        self.name = input("Enter volunteer name: ")
        self.address = input("Enter volunteer address: ")
        self.salary = float(input("Enter volunteer salary: "))

        self.payroll.add_payable(Volunteer(self.name, self.address, self.salary))
    
    def add_hourly_based_employee(self):
        self.name = input("Enter Employee name: ")
        self.address = input("Enter Employee address: ")
        self.paymnet_day = input("Enter Employee payment day: ")
        self.total_working_hours = float(input("Enter Employee total working hours: "))
        self.hourly_wage = float(input("Enter Employee hourly wage: "))

        self.payroll.add_payable(HourlyBasedEmployee(self.name, self.address, self.paymnet_day, self.total_working_hours, self.hourly_wage))

    def add_salary_based_employee(self):
        self.name = input("Enter Employee name: ")
        self.address = input("Enter Employee address: ")
        self.paymnet_day = input("Enter Employee payment day: ")
        self.salary_per_month = float(input("Enter Employee salary per month: "))

        self.payroll.add_payable(SalariedBasedEmployee(self.name, self.address, self.paymnet_day, self.salary_per_month))
    
    def add_commision_salary_based_employee(self):
        self.name = input("Enter Employee name: ")
        self.address = input("Enter Employee address: ")
        self.paymnet_day = input("Enter Employee payment day: ")
        self.salary_per_month = float(input("Enter Employee salary per month: "))
        self.sales = float(input("Enter Employee sales: "))
        self.commision_rate = float(input("Enter Employee commision rate: "))

        self.payroll.add_payable(ComissionSalariedBasedEmploee(self.name, self.address, self.paymnet_day, self.salary_per_month, self.sales, self.commision_rate))
    
    def invoice_menu(self):
        self.options = [
            "Add Book",
            "Add Notebook",
            "Exit"
            ]
        self.menu = [f"{number}- {option}" for number, option in zip(range(1, len(self.options)+1), self.options)]
        return '\n'.join(self.menu)
    
    def add_book(self):
        self.description = input("Enter book description: ") 
        self.price = int(input("Enter book price per one: "))
        self.quantity = int(input("Enter book quantity: "))
        self.author_name = input("Enter book author name: ")

        self.invoices[-1].add_item(Book(self.description, self.price, self.quantity, self.author_name))

    def add_notebook(self):
        self.description = input("Enter notebook description: ") 
        self.price = int(input("Enter notebook price per one: "))
        self.quantity = int(input("Enter notebook quantity: "))
        self.number_of_pages = int(input("Enter notebook's number of pages: "))

        self.invoices[-1].add_item(NoteBook(self.description, self.price, self.quantity, self.number_of_pages))



    def add_invoice(self):
        
        "TODO: User doesn't have to input id but it must be added automatically"
        self.invoice_id = int(input("Enter the invoice id: "))
        self.invoices.append(Invoice(self.invoice_id))
        
        while True:
            print(FrontendManager.invoice_menu(self))
            self.option = int(input("Enter the option you want to execute: "))
            if self.option == 1:
                FrontendManager.add_book(self)
            elif self.option == 2:
                FrontendManager.add_notebook(self)
            elif self.option == 3:
                break
            else:
                print("Invalid option")
                continue
        self.payroll.add_payable(self.invoices[-1])


    def display_info(self):
        print("Here is a list of all information/payables listed below: ")
        print(self.payroll)
        print(f"Total amount of money: {self.payroll.total_amount_of_money()}")
    
    def run(self):
        print("Greeting from Company Payroll Project")
        while True:
            print(FrontendManager.menu(self))
            self.option = int(input("Enter the option you want to execute: "))
            if self.option == 1:
                FrontendManager.add_volunteer(self)
            elif self.option == 2:
                FrontendManager.add_hourly_based_employee(self)
            elif self.option == 3:
                FrontendManager.add_salary_based_employee(self)
            elif self.option == 4:
                FrontendManager.add_commision_salary_based_employee(self)
            elif self.option == 5:
                FrontendManager.add_invoice(self)
            elif self.option == 6:
                FrontendManager.display_info(self)
            else:
                print("Thanks for using our system")
                print("Here's a summary of all your payables")
                FrontendManager.display_info(self)
                return
