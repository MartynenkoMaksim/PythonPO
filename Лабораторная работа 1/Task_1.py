numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_without_none = numbers[:4] + numbers[5:]
total_without_none = sum(numbers_without_none)
count_with_none = len(numbers)
average_for_none = total_without_none / count_with_none

numbers[4] = average_for_none

print("Измененный список:", numbers)
