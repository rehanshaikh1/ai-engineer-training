
def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except TypeError:
        print("Error: Please provide valid numbers.")


def convert_to_integer(value):
    try:
        number = int(value)
        print("Converted number:", number)

    except ValueError:
        print("Error: Invalid integer value.")

    finally:
        print("Conversion completed.")


divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers("10", 2)

convert_to_integer("25")
convert_to_integer("hello")
