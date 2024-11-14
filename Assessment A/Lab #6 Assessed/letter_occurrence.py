def letter_occurrence(input_string):
    count = 0

    for i in range (len(input_string)):
        if input_string[i] == "A" or input_string[i] == "a":
            count += 1
    # complete function implementation...
    return count

print(letter_occurrence("Amazing"))
print(letter_occurrence("Always aim ambitiously"))
