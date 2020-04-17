def base10 (x):
    b = 0
    rato = list(x)
    rato.reverse()
    for i in range(len(rato)):
        b = (int(rato[i]) * (2 ** i)) + b
    return b

def base3 (n,base):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, base)
        nums.append(str(r))
    return ''.join(reversed(nums))


entrada = input()

for i in range(3,10):
    print(base3(base10(entrada),i))

print(base10(entrada))



