x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
c = int(input('В какую степень хотите возвести?'))
def decorator (x,y) :
    return x+y

def step(x,y):
    n = decorator(x, y)**c
    return x+y, n

print('ступень суммы чисел x,y:')
print (step)






