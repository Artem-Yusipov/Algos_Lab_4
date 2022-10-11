import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w")


def KMP(part, string):
    M = len(part)
    N = len(string)
    inserts = list()
    lps = [0] * M
    j = 0
    prefix(part, M, lps)
    i = 0
    while i < N:
        if part[j] == string[i]:
            i += 1
            j += 1
        if j == M:
            inserts.append(i - j + 1)
            j = lps[j - 1]
        elif i < N and part[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return inserts


def prefix(pat, M, pref):
    len = 0
    pref[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            pref[i] = len
            i += 1
        else:
            if len != 0:
                len = pref[len - 1]
            else:
                pref[i] = 0
                i += 1


pattern = input()
string = input()
ans = KMP(pattern, string)
print(len(ans))
print(*ans)

