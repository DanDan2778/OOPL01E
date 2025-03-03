# Laboratory 4

# 1. Implement Conditional Statements

print()
print('1. Implement Conditional Statements: ')
x = int(input("Enter a number: "))

if x == 0:
    print('Entered Number is 0')
elif x > 0:
    print('Entered Number is Positive')
elif x < 0:
    print('Entered Number is Negative')
else:
    print('Invalid Input')

# 2. Use Loops to Process Data:

print()
print('2. Use Loops to Process Data: ')

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

while int(input('Enter a number: ')) != 0:
    pass

# Loop Control Statement

print()
print('3. Loop Control Statement')
print()
print('Skips Number Divisible by 5')
for i in range(1, 21):
    if i % 2 == 0:
        if i % 5 == 0:
            continue
        else:
            print(i)
    else:
        continue
print()
print("Stops if i is greater than 15")
for i in range(1, 21):
    if i > 15:
        break
    elif i % 2 == 0:
        if i % 5 == 0:
            continue
        else:
            print(i)
    else:
        continue

