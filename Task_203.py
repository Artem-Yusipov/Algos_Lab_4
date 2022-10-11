import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w")
s1 = input()
s2 = input()
if s1 == s2:
    print(0)
else:
    for i in range(1, len(s1)):
        s3 = s1[len(s1)-i:] + s1[0:len(s1)-i]
        if s3 == s2:
            print(i)
            break
    else:
        print(-1)

