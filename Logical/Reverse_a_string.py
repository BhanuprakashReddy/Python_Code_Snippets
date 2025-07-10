def reverse_string(s):
    """
    This function takes a string as input and returns the string reversed.
    
    :param s: The string to be reversed
    :return: The reversed string
    """

    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


s = 'abc' #'abcdefghijklmnopqrstuvwxyz'
rev = reverse_string(s)
print("Original string:", s)
print("Reverse string:", rev)
#return s[::-1]