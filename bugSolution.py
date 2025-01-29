def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numeric values
    return sum(numeric_numbers) / len(numeric_numbers)

# Correct usage handling empty list and non-numeric input
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")  # Prints 0

my_list = [1, 2, 'a']
average = calculate_average(my_list)
print(f"The average is: {average}")  # Prints 0

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}") # Prints 3.0