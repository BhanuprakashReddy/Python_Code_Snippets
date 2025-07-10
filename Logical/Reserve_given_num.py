num = 123456789

def reserve_num(num):
    rev = 0;
    while num > 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev

if __name__ == "__main__":
    print("Original number:", num)
    reversed_num = reserve_num(num)
    print("Reversed number:", reversed_num)
    if num == reversed_num:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")