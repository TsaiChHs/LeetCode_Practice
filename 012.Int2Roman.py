def intToRoman(num: int) -> str:
    # mine(num)
    # fixed(num)
    others(num)

def mine(num: int) -> str:
    romanDic = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }
    result = ""
    remain = num
    dig = 0
    while(remain > 0):
        cur = remain % 10
        remain = int(remain / 10)
        if cur >= 4:
            FIVE = romanDic[5*(10**dig)] 
        ONE = romanDic[1*(10**dig)]
        if cur == 0:
            dig += 1
            continue
        elif cur == 4:
            roman = ONE + FIVE
        elif cur == 9:
            roman = ONE + romanDic[10*(10**dig)]
        else:
            prefix = ""
            for _ in range(cur%5):
                prefix += ONE
            if cur < 4:
                roman = prefix
            else:
                roman = FIVE + prefix
        result = roman + result
        dig += 1
    return result

def fixed(num):
    pass

def others(num):
    romanDic = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    result = ''
    for nums in romanDic:
        if num >= nums:
            result += romanDic[nums] * (num // nums)
            num %= nums
    return result


if __name__ == '__main__':
    intToRoman(3)
    intToRoman(58)
    intToRoman(1994)