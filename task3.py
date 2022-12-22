# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers=[1.1, 1.2, 3.1, 5.1, 10.01]
minNum=numbers[0]%1
maxNum=numbers[0]%1

for i in range(1,len(numbers)):
    if numbers[i]%1<minNum:
        minNum=numbers[i]%1
    elif numbers[i]%1>maxNum:
        maxNum=numbers[i]%1

result=maxNum-minNum

print(f'Разница между максимальным {round(maxNum,4)} и минимальным значением {round(minNum,4)} дробной части чисел равно: {round(result,4)}')