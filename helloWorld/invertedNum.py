original = 356
inverted = 0

while original != 0:
    inverted = inverted * 10 + (original % 10)
    original = original // 10
else:
    print("that's enough")

print(inverted)
