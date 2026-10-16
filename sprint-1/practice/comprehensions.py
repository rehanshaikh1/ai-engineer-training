
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]
print("Squares:", squares)

even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

odd_numbers = [number for number in numbers if number % 2 != 0]
print("Odd numbers:", odd_numbers)

names = ["rehan", "aditya", "rahul", "aman"]

uppercase_names = [name.upper() for name in names]
print("Uppercase names:", uppercase_names)

long_names = [name for name in names if len(name) > 4]
print("Long names:", long_names)

prices = [100, 250, 500, 750, 1000]

discounted_prices = [price * 0.9 for price in prices]
print("Discounted prices:", discounted_prices)

number_squares = {
    number: number ** 2
    for number in range(1, 6)
}
print("Number squares:", number_squares)

number_types = {
    number: "Even" if number % 2 == 0 else "Odd"
    for number in numbers
}
print("Number types:", number_types)

employees = [
    {"name": "Rehan", "department": "IT"},
    {"name": "Aditya", "department": "HR"},
    {"name": "Rahul", "department": "IT"},
    {"name": "Aman", "department": "Finance"}
]

it_employees = [
    employee["name"]
    for employee in employees
    if employee["department"] == "IT"
]
print("IT employees:", it_employees)
