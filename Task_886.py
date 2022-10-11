import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w")
s = input()
n = len(s)
prefix = [0 for i in range(1 + n)]
l = 0
for i in range(1, n):
    while True:
        if s[l] == s[i]:
            l += 1
            break
        if l == 0:
            break
        l = prefix[l]
    prefix[i + 1] = l
period = n - prefix[n]
if n % period != 0:
    ans = 1
else:
    ans = n // period
print(ans)




