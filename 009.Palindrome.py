# Require: Solve without concerting Int to Str

def palindrome(x): # True / False
    y = 0 # let y = x reverse
    tmp = x
    i = 0
    while tmp != 0:
        y = y*10 + (tmp % 10) # get last digit
        tmp = int(tmp/10)
        i += 1
    return x == y

if __name__ == '__main__':
    print(palindrome(121))
    print(palindrome(123))
    print(palindrome(-121))












