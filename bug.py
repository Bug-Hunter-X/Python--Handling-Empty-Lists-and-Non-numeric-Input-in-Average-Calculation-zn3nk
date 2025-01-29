def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    return sum(numbers) / len(numbers)

# Incorrect usage leading to ZeroDivisionError
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") # This will print 0 as expected

#However, if you modify it to:
my_list = []
#The function doesn't handle non-numeric input or other edge cases.
if len(my_list) == 0:
    print("List is empty")
else:
    average = calculate_average(my_list)
    print(f"The average is: {average}")  # This still prints 0

#another edge case:
my_list = [1,2,'a']
average = calculate_average(my_list) #This will throw an error
print(f"The average is: {average}")