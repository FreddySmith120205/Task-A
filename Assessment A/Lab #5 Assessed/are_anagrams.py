def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    
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

## Example 
print(are_anagrams("listen", "silent"))  # Expected output: True
print(are_anagrams("hello", "world"))    # Expected output: False
