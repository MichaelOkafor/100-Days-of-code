numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Remember for conditional list comprehension [new_item for item in list if test]
result = [num for num in numbers if num % 2 == 0]

print(result)
