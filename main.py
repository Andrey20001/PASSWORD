import random

list = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lll = int(input("Какой длины сгенерировать пароль? "))

password = ""

for i in range(lll):
    password += list[random.randint(0, len(list) - 1)]

print("Ваш пароль:", password)
