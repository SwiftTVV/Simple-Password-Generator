import random

# ALL Strings that can be used in a password

uppercase_letters = "ABCDEFGIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[],.;:-/\\?!*#@<>^"

# Booleans

upper, lower, nums, syms = True, True, True, True

# Final Password

all = ""

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols

length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
