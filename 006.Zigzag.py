def convert(s, numRows):
    # mine(s, numRows)
    sortByRow(s, numRows)

def sortByRow(s, numRows):
    if numRows == 1: return s
    queue = ["" for _ in range(max(numRows, len(s)))]
    curRow, goDown, output = 0, False, ""
    for c in s:
        queue[curRow] += c
        print(curRow)
        if curRow == numRows-1 or curRow <= 0:
            goDown = not goDown
        if goDown: curRow += 1
        else: curRow -= 1
    for ss in queue:
        output += ss
    return output
        
def visitByRow(s, numRows):
    if numRows == 1: return s
    cycleLen = 2*numRows - 2
    pass

def mine(s, numRows):
    if numRows == 1:
        return s
    step, cur = 0, 0
    queue = ["" for _ in range(numRows)]
    while cur < len(s):
        step = step % (numRows-1)
        if step == 0:
            for i in range(numRows):
                if cur >= len(s): break
                queue[i] += s[cur]
                cur += 1
        else:
            queue[numRows - step -1] += s[cur]
            cur += 1
        step += 1
    output = ""
    for i in range(numRows):
        output += queue[i]
    return output
if __name__ == '__main__':
    print(convert("PAYPALISHIRING", 4))
    print()
    print(convert("PAYPALISHIRING", 3))
    print()
    print(convert("A", 1))