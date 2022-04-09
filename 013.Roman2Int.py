def romanToInt(s: str) -> int:
    # mine(s)
    reversed(s)

ROMANs = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
def mine(s: str) -> int:
    pre, result, buffer = "", 0, 0
    for c in s:
        if not pre or ROMANs[c] < ROMANs[pre]:
            result += buffer
            buffer = 0
        elif ROMANs[c] > ROMANs[pre]:
            result -= buffer
            buffer = 0
        pre = c
        buffer += ROMANs[c]
    result += buffer
    return result

def reversed(s: str) -> int:
    pre, result = "", 0
    for c in s[::-1]:
        if pre and ROMANs[c] < ROMANs[pre]: # 反常
            result -= ROMANs[c]
        else:
            result += ROMANs[c]
        pre = c
    return result 
if __name__ == '__main__':
    romanToInt("III")
    romanToInt("LVIII")
    romanToInt("MCMXCIV")