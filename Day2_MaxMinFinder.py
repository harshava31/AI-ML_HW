numbers = [23, 45, 12, 67, 8, 90, 34]

# Initialize max and min with the first element of the list
max_val = numbers[0]
min_val = numbers[0]

# Iterate through the list starting from the second element
for num in numbers[1:]:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(f"List: {numbers}")
print(f"Maximum Value: {max_val}")
print(f"Minimum Value: {min_val}")