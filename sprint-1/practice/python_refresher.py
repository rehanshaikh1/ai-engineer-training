
name = "Rehan"
age = 20
rating = 4.5
is_available = True

print("Name:", name)
print("Age:", age)
print("Rating:", rating)
print("Available:", is_available)

age_string = "20"
age_number = int(age_string)

rating_string = "4.5"
rating_number = float(rating_string)

print("Converted age:", age_number)
print("Converted rating:", rating_number)

issues = [
    "Wi-Fi not working",
    "Login problem",
    "Email not working",
    "Printer issue"
]

for issue in issues:
    print(issue)

print("First issue:", issues[0])

employee = {
    "name": "Rehan",
    "department": "IT",
    "issue": "Wi-Fi not working",
    "priority": "High"
}

print(employee["name"])
print(employee["department"])
print(employee["issue"])

employee["status"] = "Open"
print(employee)

def greet_user(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

print(greet_user("Rehan"))
print("Sum:", add_numbers(10, 20))

class ITSupport:
    def __init__(self, employee_name, issue):
        self.employee_name = employee_name
        self.issue = issue
        self.status = "Open"

    def show_details(self):
        print("\nTicket Details")
        print("Employee:", self.employee_name)
        print("Issue:", self.issue)
        print("Status:", self.status)

    def resolve_ticket(self):
        self.status = "Resolved"
        return f"Ticket for {self.employee_name} is resolved."

ticket = ITSupport("Rehan", "Laptop not connecting to Wi-Fi")

ticket.show_details()
print(ticket.resolve_ticket())
ticket.show_details()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", even_numbers)

number_squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(number_squares)

priority = "High"

if priority == "High":
    print("High-priority ticket")
elif priority == "Medium":
    print("Medium-priority ticket")
else:
    print("Low-priority ticket")

user_input = "25"

try:
    number = int(user_input)
    result = 100 / number
    print("Division result:", result)

except ValueError:
    print("Invalid input: enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Exception handling completed.")

def get_integer(value):
    try:
        return int(value)
    except ValueError:
        print(f"Invalid integer: {value}")
        return None

print(get_integer("123"))
print(get_integer("hello"))

tickets = [
    {"id": 1, "issue": "Wi-Fi", "priority": "High"},
    {"id": 2, "issue": "Email", "priority": "Low"},
    {"id": 3, "issue": "Login", "priority": "High"},
    {"id": 4, "issue": "Printer", "priority": "Medium"}
]

high_priority_tickets = [
    ticket for ticket in tickets
    if ticket["priority"] == "High"
]

for ticket in high_priority_tickets:
    print(ticket)
