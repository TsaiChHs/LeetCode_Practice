def reverseInt(x):
    mine(x)
    # toStr(x)

def mine(x):
    MAX_INT = 2**31
    output, operator = 0, 1
    if x < 0:
        operator = -1 
        x = x * (-1)
    while x != 0:
        output = output * 10 + x % 10
        x = int(x / 10)
        if output*operator >  MAX_INT-1 or output*operator < -(2**31): return 0
    return output*operator

def toStr(x):
    negative = x < 0
    if negative: x = x * (-1)
    strX = str(x)
    output = int(strX[::-1])
    if negative: output = output * (-1)
    if output > 2**31 - 1 or output < -(2**31): output = 0
    return output

if __name__ == '__main__':
    reverseInt(123)
    reverseInt(-123)
    reverseInt(120)