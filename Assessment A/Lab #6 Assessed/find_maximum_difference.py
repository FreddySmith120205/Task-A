def find_maximum_difference(a, b):
    if (max(a) - min(b)) > (max(b) - min(a)):
        maximum = (max(a) - min(b))
    else:
        maximum = (max(b) - min(a))

    
    
#     # code implementation here...
    return maximum



print(find_maximum_difference([1,5 ,600], [100 ,7, 3 , 29, 39]))
print(find_maximum_difference([1,5 ,600], [100 ,7, 3 , 602, 39])) # returns 60