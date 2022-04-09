# 用 Sliding Window 太耗時間 --> 因為一直改變 window size, then 做重複的動作
# 想想看有沒有可以掃一遍就找到最佳解的方式

def longestPalindrome(s):
    dynamic_programming(s)
    # manacher(s)

# My Approach
def sliding_window(s):
    # sliding window from large to small
    for wSize in range(len(s), 0, -1):
        for cur in range(len(s)-wSize+1):
            curWin = s[cur:cur+wSize]
            if curWin == curWin[::-1]:
                return curWin
    return ""


# Approach 1
def dynamic_programming(s):
    # Every Character as a center to span
    pLen = []
    for i in range(len(s)):
        if i-1 >= 0 and s[i] == s[i-1] and i+1 < len(s) and s[i] == s[i+1]:
            curL, curR = i-1, i+1
            pLen.append([3, s[curL:curR+1]])
        elif i-1 >= 0 and s[i] == s[i-1]:
            curL, curR = i-1, i
            pLen.append([2, s[curL:curR+1]])
        elif i+1 < len(s) and s[i] == s[i+1]:
            curL, curR = i, i+1
            pLen.append([2, s[curL:curR+1]])
        else:
            curL, curR = i-1, i+1
            pLen.append([1, s[i]])
        while curL >= 0 and curR < len(s):
            if s[curL] != s[curR]:
                break
            pLen[i][0] += 2
            pLen[i][1] = s[curL:curR+1]
            curL, curR = curL-1, curR+1
    return sorted(pLen, reverse=True)[0][1]
        
# Approach 2
def manacher(s):
    new_s = "_"
    for i in s:
        new_s += i + "_"
    radius = [[i, 1] for i in range(len(new_s))]
    for i in range(len(new_s)):
        curL, curR = i-1, i+1
        while curL >= 0 and curR < len(new_s):
            if new_s[curL] != new_s[curR]:
                break
            radius[i][1] += 1
            curL, curR = curL-1, curR+1
    maxSet = sorted(radius, key = lambda s: s[1], reverse=True)[0]
    result = new_s[maxSet[0]-maxSet[1]+1 : maxSet[0]+maxSet[1]-1]
    return result.replace("_", "")

if __name__ == "__main__":
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("a"))
    print(longestPalindrome("ac"))