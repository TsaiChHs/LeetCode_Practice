import math

def myAtoi(s):
    mine(s)

def mine(s):
    MAX_INT = 2**31
    MAX_INT_DIGIT = math.log(MAX_INT, 10)
    operator, isSet, num = 1, False, ""
    pre = ""
    for c in s:# for each char in s
        print("c={}, num={}, len={}".format(c, num, len(num)))
        if not isSet and c == '-': # if == "-", mark the num as negative
            operator = -1
            isSet = True
            isNum = not isNum
        elif not isSet and c == '+':
            isSet = True
            isNum = not isNum
        elif c == " " or (len(num) == 0 and c == '0'):
            isNum
            pass
        elif c >= '0' and c <= '9':
            num += c
        else:
            break
        if len(num) == MAX_INT_DIGIT: # if len == digit of math_Int
            break
    if num == "":
        result = 0
    else:
        result = int(num)*operator
        if result > MAX_INT-1:
            result = MAX_INT - 1
        elif result < -MAX_INT: # Convert it to int and check if it is over the range of In32
            result = -MAX_INT
    return result # return the result

if __name__ == "__main__":
    # myAtoi("42")
    # myAtoi("0032")
    # myAtoi("      -42")
    myAtoi("4193 with words")