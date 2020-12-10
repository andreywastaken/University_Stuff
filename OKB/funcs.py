import math


# Частное и остаток
def div_mod(a, b):
    q = a // b
    r = a - q * b
    print(f'{q};{r}')


# Проверяет простое ли число
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f'{num} / {i} =', num / i)
            return False
    return True


# a mod b
def mod(a, b):
    print(a % b)


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


# инверсия ax mod m = 1
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return('нет')
    else:
        return x % m

# Нод
def gcd(a, b):
    return math.gcd(a, b)


def __cez(n):
    ks = []
    for i in range(1, n + 1):
        flag = True
        coded = []
        for mi in range(0, n):
            ci = (mi * i) % n
            if ci in coded:
                flag = False
                break
            coded.append(ci)
        if flag:
            ks.append(i)
    for k in ks:
        if modinv(k, n) not in ks:
            ks.remove(k)
    return ks


# Цезарь Ci = Mi * k mod n
def cez(n):
    ks = __cez(n)
    for i in range(len(ks) - 1):
        print(f'{ks[i]};', end='')
    print(ks[-1])

def __all_modinv(n):
    res = []
    for i in range(1, n + 1):
        tempinv = modinv(i, n)
        if(tempinv != 'нет'):
            res.append((i, tempinv))
    return res


# Все пары чисел в инверсии Zn
def all_modinv(n):
    all = __all_modinv(n)
    for i in range(0, len(all) - 1):
        print(f'({all[i][0]};{all[i][1]});', end='')
    print(f'({all[-1][0]};{all[-1][1]})')

# Ключи которые не подходят для n из Ci Mi * k mod n
def ne_cez(n):
    ks = __cez(n)
    notks = [x for x in range(1, n) if x not in ks]
    if len(notks) == 0:
        print('нет')
        return
    for i in range(0, len(notks) - 1):
        print(f'{notks[i]};', end='')
    print(notks[-1])


# Все элементы множества Zn, n > 0
def Z(n):
    if(n < 1):
        return
    for i in range(0, n - 1):
        print(f'{i};', end='')
    print(n - 1)


# Вычислите выражение a^b в Zn
def exp1(a, b, n):
    print(a**b % n)


# Вычислите выражение a - b/c + d в Zn
def exp2(a, b, c, d, n):
    print((a - b * modinv(c, n) + d) % n)

exp2(197, 200, 19, 153, 10)


# Друзья пифагора: n - кол-во друзей, f - кол-во фиников
def bros(n, f):
    print(f % n)


# Мем с евклидом
def evk(n):
    facts = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            facts.append(i)
            n //= i
        i += 1
    if n > 1:
        facts.append(n)

    for i in range(len(facts) - 1):
        print(f'{facts[i]};', end='')
    print(facts[-1])


def gamma(c, key):
    c = bytearray.fromhex(c)
    for i in c:
        print(chr(i ^ key), end='')
    print()


gamma("607a13657a6013637270767e1f136372617213796660677a677a727e", 0x33)
