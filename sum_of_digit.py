# sum of the digit using recursion ---->


def sumOfdigit(n):
    assert n >= 0 and n == int(n) , "The number should be a positive integer !!!" 
    if n == 0 :
        return 0
    else:
        return n%10 + sumOfdigit(n//10)


print(sumOfdigit(123111))