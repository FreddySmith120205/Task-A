def calculator(num1, num2, operator):

    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"The result is: {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"The result is: {result}")
    elif operator == "/":
        if num2 == 0:
            print("Error")
            return "Error"
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    elif operator == "%":
        if num2 == 0:
            print("Error")
            return "Error"
        else:
            result = num1 % num2
            print(f"The result is: {result}")
    elif operator == ">":
        result = num1 > num2
        print(f"The result is: {result}")
    elif operator == "<":
        result = num1 < num2
        print(f"The result is: {result}")
    elif operator == ">=":
        result = num1 >= num2
        print(f"The result is: {result}")
    elif operator == "<=":
        result = num1 <= num2
        print(f"The result is: {result}")
    else:
        print("Invalid operator.")
        return "Invalid operator"

    return result

def max_of_three(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        maximum = num1
    elif num2 > num1 and num2 > num3:
        maximum = num2
    else:
        maximum = num3

    return maximum

def winning_numbers(user_list, winning_list):

    count = 0

    if user_list[0] == winning_list[0] or user_list[0] == winning_list[1] or user_list[0] == winning_list[2]:
        count += 1
    if user_list[1] == winning_list[0] or user_list[1] == winning_list[1] or user_list[1] == winning_list[2]:
        count += 1
    if user_list[2] == winning_list[0] or user_list[2] == winning_list[1] or user_list[2] == winning_list[2]:
        count += 1

    if count == 1:
        prize = "Third"
    elif count == 2:
        prize = "Second"
    elif count == 3:
        prize = "First"
    else:
        prize = "No"
    # Print the result
    print(f"Congratulations, you won {prize} prize!")
    return prize

def are_anagrams(str1, str2):

    
    l1 = list(str1)
    l2 = list(str2)
    if len(l1) != len(l2):
        output = False
    else:
        sort1 = sorted(l1)
        sort2 = sorted(l2)
        if sort1 != sort2:
            output = False
        else:
            output = True

    return output

def calculate_average(numbers):

    total = 0
    length = len(numbers)
    for i in numbers:
        total += i
    average = total / length
    
        



    return average

def calculate_weekly_pay(hours_worked):

    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    if hours_worked > standard_hours:
        overtime_hours = hours_worked - standard_hours
        total_pay = (regular_rate * standard_hours) + (overtime_rate * overtime_hours)
    else:
        total_pay = regular_rate * hours_worked



    return total_pay
    
def is_prime(num):
    if num == 2:
        output = True
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                output = False
                break
            else:
                output = True  
    else:
        output = False
    return output

def sum_of_evens(min_value, max_value):

    total = 0

    for i in range (min_value, max_value+1):
        if i % 2 == 0:
            total = total + i
        


    
    
    return total

def celsius_to_fahrenheit(celsius):
   output = ((celsius * 9/5) + 32)
   # complete your function implementation... 
   return output

def decrypt_cypher_text(encrypted_text, key):
    if key < 0:
        print("Key must be a positive number")
        return
    
    else:

        decrypted_text = ""

        for character in encrypted_text:
            ASCII_text = ord(character)
            x = (ASCII_text - key) % 256
            decrypted_text += chr(x)
#     # function implementation here...
    return decrypted_text

def find_maximum_difference(a, b):
    if (max(a) - min(b)) > (max(b) - min(a)):
        maximum = (max(a) - min(b))
    else:
        maximum = (max(b) - min(a))

    
    
#     # code implementation here...
    return maximum

def fuel_cost(distance_miles):
    PRICE_PER_LITER = 1.49
    MPG = 50
    LITERS_PER_GALLON = 4.5
    if distance_miles >= 0:
        total_cost = (PRICE_PER_LITER * (distance_miles / MPG) * LITERS_PER_GALLON)
    else:
        print("Distance can't be negative")
     
#     continue function implementation here...
    return total_cost

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

def km_to_miles(kilometers):
    if kilometers >= 0:
        miles = kilometers * 0.62
        miles = round(miles, 3)
    else:
        print("Original number must be positive")
    

    # complete function implementation here...
    return miles

def letter_occurrence(input_string):
    count = 0

    for i in range (len(input_string)):
        if input_string[i] == "A" or input_string[i] == "a":
            count += 1
    # complete function implementation...
    return count

def annual_net_income(gross_salary):
    if gross_salary >= 45000:
        tax_rate = 1/2
    elif gross_salary < 45000 and gross_salary >= 30000:
        tax_rate = 3/10
    else:
        tax_rate = 3/20

    net_salary = gross_salary * (1 - tax_rate)
    # complete your function implementation here...
    return net_salary