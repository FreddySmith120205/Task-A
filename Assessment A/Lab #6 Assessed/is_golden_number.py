def is_golden_number(n):
    
    if n < 1000 and n > 0:

        for x in range(1, n):
            boolean = False
            y = n - x

            if x * y % 1000 == 0:
                boolean = True
                break
    else:
        print("Number must be positive and less than 1000")


    return boolean

print(is_golden_number(61))
print(is_golden_number(65))
print(is_golden_number(70))

