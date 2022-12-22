# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n=int(input('Введите число n=: '))
fibonachi=[]
fibonachi.append(0)
fibonachi.append(1)
for i in range(2,n+1):
    fibonachi.append(fibonachi[i-2]+fibonachi[i-1])


x=1
for i in range(0,n):
    if x%2>0:
        fibonachi.insert(0,fibonachi[i+x])
    else:
        fibonachi.insert(0,-fibonachi[i+x])
    x+=1
    
print(fibonachi)