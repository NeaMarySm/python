# Задача 26:

# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


num = int(input("enter number: "))
val = int(input("enter pow: "))


def pow(a, b):
    if b == 0:
        return 1
    if b > 0:
        return a * pow(a, b-1)
    else:
        return 1/a * pow(a, b+1)


result = pow(num, val)
print(result)
