for num in range(-5, 6):

    if num == 0:
        continue
    elif num > 0:
        print(f'{num} is a Positive Number')
        if num % 2 == 0:
            break
    else:
        print(f'{num} is a Negative Number')
pass


