from calculator import Calculator


if __name__ == "__main__":
    calculator = Calculator()
    first_number = 10
    second_number = 3

    print(f"{first_number} + {second_number} = {calculator.add(first_number, second_number)}")
    print(f"{first_number} - {second_number} = {calculator.subtract(first_number, second_number)}")
    print(f"{first_number} * {second_number} = {calculator.multiply(first_number, second_number)}")
