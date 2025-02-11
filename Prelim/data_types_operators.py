# Task 1
print('Task 1')

integer = 19
float_number = 8.2
complex_number = complex(3, 5)
string_data = "This is a String"
list_data = [1, 2, 3, 4, 5]
tuples_data = ('dan', 'niel', 'agus', 'tin')
set_data = {'compute', 'mouse', 'keyboard'}
frozen_set_data = frozenset(set_data)
dict_data = {
    'Name': 'Daniel',
    'Age': 19,
    'Date of Birth': 'August 16, 2005'
}
bool_data = 10 == 0
none_data = None


print(type(integer))
print(type(float_number))
print(type(complex_number))
print(type(string_data))
print(type(list_data))
print(type(list_data))
print(type(tuples_data))
print(type(set_data))
print(type(frozen_set_data))
print(type(dict_data))
print(type(bool_data))
print(type(none_data))

#------------------------------------------------------#

#Task 2

print('------------------------------------------------------')
print('Task 2')

add = 1 + 1
add2 = 7.8 + 6.5

subtract = 7 - 3
subtract2 = 7.8 + 6.5

multiply = 7 * 3
multiply2 = 7.4 * 4.56

divide = 7/3.5
divide2 = 7/3.56

print('Integers:')
print(add)
print(subtract)
print(multiply)
print(divide)

print('Floating Numbers:')
print(add2)
print(subtract2)
print(multiply2)
print(divide2)

print('Concatenate(join): ')
string1 = 'Hello'
string2 = 'World!'
string1 += " " + string2
print(string1)

print('Split String:')
split_string1 = string1.split()
print(split_string1)

print('Add and Remove Items in List:')
list_data = [6, 5, 4, 3, 2, 1]
list_data.append(0)
print('add item: ',list_data)
list_data.remove(6)
print('remove item: ', list_data)

print('Access Values from a dictionary:')
dict_data = {
    'Name': 'Daniel',
    'Age': 19,
    'Date of Birth': 'August 16, 2005'
}
print(dict_data['Name'])
print(dict_data['Age'])
print(dict_data['Date of Birth'])

#------------------------------------------------------#

#Task 3

print('------------------------------------------------------')
print('Task 3')

# Using Operators
x = 1
# o	Create a program that accepts two integer inputs and performs the following:
while x != 0:
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    print('Operations: +, -, *, /, %, **, //, ==, !=, >, <, >=, <=, and, or, not')
    operation = input('Enter operation: ')

    # arithmetic operations
    if x == 0 & y == 0:
        break
    elif operation == '+':
        print(f'Arithmetic: {x} + {y} = {int(x) + int(y)}')
    elif operation == '-':
        print(f'Arithmetic: {x} - {y} = {int(x) - int(y)}')
    elif operation == '*':
        print(f'Arithmetic: {x} * {y} = {int(x) * int(y)}')
    elif operation == '/':
        print(f'Arithmetic: {x} / {y} = {int(x) / int(y)}')
    elif operation == '%':
        print(f'Arithmetic: {x} % {y} = {int(x) % int(y)}')
    elif operation == '**':
        print(f'Arithmetic: {x} ** {y} = {int(x) ** int(y)}')
    elif operation == '//':
        print(f'Arithmetic: {x} // {y} = {int(x) // int(y)}')

    # comparison operations
    elif operation == '==':
        print(f'Comparison: {x} == {y} = {int(x) == int(y)}')
    elif operation == '!=':
        print(f'Comparison: {x} != {y} = {int(x) != int(y)}')
    elif operation == '>':
        print(f'Comparison: {x} > {y} = {int(x) > int(y)}')
    elif operation == '<':
        print(f'Comparison: {x} < {y} = {int(x) < int(y)}')
    elif operation == '>=':
        print(f'Comparison: {x} >= {y} = {int(x) >= int(y)}')
    elif operation == '<=':
        print(f'Comparison: {x} <= {y} = {int(x) <= int(y)}')

    # logical operations
    elif operation == 'and':
        print(f'Logical: {x} and {y} = {int(x) and int(y)}')
    elif operation == 'or':
        print(f'Logical: {x} or {y} = {int(x) or int(y)}')
    elif operation == 'not':
        print(f'Logical: not {x} = {not int(x)}')
        print(f'Logical: not {y} = {not int(y)}')

    # bitwise operations
    elif operation == '&':
        print(f'Bitwise: {x} & {y} = {int(x) & int(y)}')
    elif operation == '|':
        print(f'Bitwise: {x} | {y} = {int(x) | int(y)}')
    elif operation == '^':
        print(f'Bitwise: {x} ^ {y} = {int(x) ^ int(y)}')
    elif operation == '~':
        print(f'Bitwise: ~{x} = {~int(x)}')
        print(f'Bitwise: ~{y} = {~int(y)}')
    elif operation == '<<':
        print(f'Bitwise: {x} << {y} = {int(x) << int(y)}')
    elif operation == '>>':
        print(f'Bitwise: {x} >> {y} = {int(x) >> int(y)}')
    else:
        print('Invalid operation')

#------------------------------------------------------#

#comparison operators

