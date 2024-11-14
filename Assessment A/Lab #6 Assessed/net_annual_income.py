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
        


print(annual_net_income(60000))
print(annual_net_income(30000))
print(annual_net_income(20000))

