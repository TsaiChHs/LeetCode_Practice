
def lengthOfLongestSubstring(s):
    # check from big window to small window
    for wSize in range(len(set(s)), 0, -1):
        for cur in range(len(s)-wSize+1):
            curWin = s[cur:cur+wSize]
            print("Cur={}, wSize={}, curWin={}".format(cur, wSize, curWin))
            # if there isn't any duplicate char in the window
            if len(curWin) == len(set(curWin)):
                return len(curWin)
    return 0
    
if __name__ == '__main__':
    print("Result: {}".format(lengthOfLongestSubstring("abcabcbb")))
    print("Result: {}".format(lengthOfLongestSubstring("bbbb")))
    print("Result: {}".format(lengthOfLongestSubstring(" ")))
    print("Result: {}".format(lengthOfLongestSubstring("aregvdfnjkjhfgedsdddfssdfsdaewethjnf")))
    f = open('003.testData.txt', mode='r')
    print("Result: {}".format(lengthOfLongestSubstring(f.read().strip('"'))))