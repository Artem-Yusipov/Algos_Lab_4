import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w")
s1 = input()
s2 = input()
count1 = [0 for i in range(128)]
count2 = [0 for j in range(128)]
for c in s1:
    count1[ord(c)] += 1
for c in s2:
    count2[ord(c)] += 1
ans = ''
pos1 = 0
pos2 = 0
for c in "zyxwvutsrqponmlkjihgfedcba":
    while count1[ord(c)] > 0 and count2[ord(c)] > 0:
        ans += c
        while s1[pos1] != c:
            count1[ord(s1[pos1])] -= 1
            pos1 += 1
        count1[ord(s1[pos1])] -= 1
        pos1 += 1
        while s2[pos2] != c:
            count2[ord(s2[pos2])] -= 1
            pos2 += 1
        count2[ord(s2[pos2])] -= 1
        pos2 += 1
print(ans)


