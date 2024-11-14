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

print(fuel_cost(50))

