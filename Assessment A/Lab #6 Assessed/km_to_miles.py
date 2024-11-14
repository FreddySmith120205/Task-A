def km_to_miles(kilometers):
    if kilometers >= 0:
        miles = kilometers * 0.62
        miles = round(miles, 3)
    else:
        print("Original number must be positive")
    

    # complete function implementation here...
    return miles


print(km_to_miles(120))