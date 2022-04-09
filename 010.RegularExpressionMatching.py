def regExpMatch(s, p):
    ansRecur(s, p)

def mine(s, p):
    s_cur, p_cur = 0, 0
    while p_cur < len(p) and s_cur < len(s):

        if p_cur + 1 < len(p) and p[p_cur+1] == '*':
            p_end, s_end = p_cur+2, s_cur
            if p[p_cur] == '.':
                if p_end == len(p):
                    s_cur = len(s)
                    p_cur = p_cur+1
                    break
                while p_end < len(p) and s_end < len(s) and p[p_end] != s[s_end]:
                    s_end += 1
            else:
                while p_end < len(p) and s_end < len(s) and p[p_end] == s[s_end]:
                    p_end += 1
                    s_end += 1
                if (s_end - s_cur) - (p_end - p_cur) < 0:
                    break
            p_cur = p_end
            s_cur = s_end

        elif p[p_cur] == s[s_cur]:
            p_cur += 1
            s_cur += 1
        else:
            break

    if p_cur == len(p) and s_cur == len(s):
        print(True)
        return True
    else:
        print(False)
        return False

def ansRecur(s: str, p: str) -> bool:
    if not p:
        return not s

    isMatch = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        return ansRecur(s, p[2:]) or (isMatch and ansRecur(s[1:], p))
                
    else:
        return isMatch and ansRecur(s[1:], p[1:])

if __name__ == '__main__':
    regExpMatch("aa", "a*")
    regExpMatch("aa", "a")
    regExpMatch("ab", ".*")