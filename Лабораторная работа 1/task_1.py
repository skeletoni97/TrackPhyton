numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missingItem = 4
SumNumbers = sum(numbers[:missingItem] + numbers[missingItem+1:])
averageOfNumbers = SumNumbers / len(numbers)
numbers[4] = averageOfNumbers

print("Измененный список:", numbers)


