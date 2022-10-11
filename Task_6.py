import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w")


def z_function(string):
    z = [0 for i in range(len(string))]
    left = right = 0
    for i in range(1, len(string)):
        if i >= right:
            j = 0
            while i + j < len(string) and string[i + j] == string[j]:
                j += 1
            left = i
            right = i + j
            z[i] = j
        else:
            if z[i - left] < right - i:
                z[i] = z[i - left]
            else:
                j = right - i
                while i + j < len(string) and string[i + j] == string[j]:
                    j += 1
                left = i
                right = i + j
                z[i] = j

    print(" ".join(list(map(str, z[1:]))))


m = input()
z_function(m)




