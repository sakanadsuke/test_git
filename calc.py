def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

val_1 = input('input first number: ')
val_2 = input('input second number: ')

value_sum = sum(int(val_1), int(val_2))
print("")

print("the result of sum =")
print(value_sum)

value_subtract = subtract(int(val_1), int(val_2))

print("the result of subtract =")
print(value_subtract)

