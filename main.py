import random

list = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lll = int(input("Какой длины сгенерировать пароль? "))

password = ""

for i in range(lll):
    password += random.choice(list)

print("Ваш пароль:", password)
