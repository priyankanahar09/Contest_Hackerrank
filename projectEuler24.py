def factorial_fill():
    fact = [0] * 14
    fact[0] = 1
    for i in range(1, 14):
        fact[i] = i * fact[i - 1]
    return fact

def factorial_num(n, arrc):
    tmp = n
    index = 0
    for i in range(13, -1, -1):
        if fact[i] <= tmp:
            index = i
            break

    q, r = 0, 0
    while index >= 0:
        q = tmp // fact[index]
        r = tmp % fact[index]
        arrc[index] = q
        tmp = r
        index -= 1

def update_list(char_list, index):
    for i in range(index + 1, 13):
        char_list[i - 1] = char_list[i]

def print_permutation(arrc):
    char_list = list("abcdefghijklm")
    for i in range(12, -1, -1):
        print(char_list[arrc[i]], end='')
        update_list(char_list, arrc[i])
    print()

if __name__ == "__main__":
    fact = factorial_fill()

    t = int(input())
    for _ in range(t):
        n = int(input())
        arrc = [0] * 13
        factorial_num(n - 1, arrc)
        print_permutation(arrc)
