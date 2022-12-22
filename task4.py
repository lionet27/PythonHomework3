# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n=int(input('Введите число n=: '))
decimalNum=[]

while n!=1:
    decimalNum.append(n%2)
    n=n//2
decimalNum.append(n)

numDec=decimalNum[-1]

for i in range(-2,-len(decimalNum)-1,-1):
    numDec=numDec*10+decimalNum[i]

print(f"Число n будет в двоичной системе выглядеть так: {numDec}")
