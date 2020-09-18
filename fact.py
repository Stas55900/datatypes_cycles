num = int(input('Число: '))
dot = 1
while num != 1:
    dot *= num
    num -= 1
print(dot)