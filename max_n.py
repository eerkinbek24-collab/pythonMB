# фанкшн 
def get_numbers():
    numbers = []
    n = int(input("How many numbers do you want to enter? "))
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    return numbers

# функция кт на мак
def find_maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# функция кт на мин 
def find_minimum(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def main():
    print("=" * 40)
    print("   FIND THE MAXIMUM NUMBER")
    print("=" * 40)

    numbers = get_numbers()

    print("\nYour numbers:", numbers)
    print("-" * 40)
    print("Maximum number:", find_maximum(numbers))
    print("Minimum number:", find_minimum(numbers))

    print("-" * 40)

main()
