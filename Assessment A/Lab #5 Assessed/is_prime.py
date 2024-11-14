def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                output = False
                break
            else:
                output = True  
    else:
        output = False
            



    return output


# # # Run code example
boolean = is_prime(5)   # returns True
print(boolean)
  