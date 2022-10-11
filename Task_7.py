import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w")


def hash_table(string):
    hashes = []
    for i in range(len(string)):
        res = []
        cont = 10 ** 9 + 9
        sm_str = string[0: len(string) - i]
        sm_hash = hash(sm_str)
        res.append([0, len(sm_str), sm_hash])
        for j in range(1, len(string) - len(sm_str) + 1):
            sum_1 = (sm_hash - (ord(string[j - 1]) * (13 ** (len(sm_str) - 1) % cont)) % cont) * 13
            sum_2 = ord(string[j + len(sm_str) - 1])
            sm_hash = (sum_1 + sum_2) % cont
            res.append([j, len(sm_str), sm_hash])
        hashes.append(res)
    return list(reversed(hashes))


def hash(string):
    cont = 10 ** 9 + 9
    hash = 0
    for i in string:
        hash = (hash * 13 + ord(i)) % cont
    return hash


def compare(string1, string2):
    table_1 = hash_table(string1)
    table_2 = hash_table(string2)
    for i in range(min(len(string1), len(string2)), 0, -1):
        for j in table_1[i - 1]:
            for t in table_2[i - 1]:
                if j[2] == t[2]:
                    sub_str = string1[j[0]: j[0] + j[1]]
                    return j[0], t[0], len(sub_str), sub_str
    return 0, 0, 0


string1, string2 = input().split()
print(*compare(string1, string2))


