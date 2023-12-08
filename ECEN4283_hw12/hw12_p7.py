
"""
(a) Using RSA, choose p = 3 and q = 11, and encode the word “dog” by encrypting each letter separately.
 Apply the decryption algorithm to the encrypted version to recover the original plaintext message.

(b) Repeat part (a) but now encrypt “dog” as one message m.

dog - > [d, o, g] -> [4, 15, 7] -> [00100, 01111, 00111]
convert dog to 5 bit binary (26 letters in alphabet)
"""
# ==================================================================
# part a
# ==================================================================

# given
p, q = 3, 11

n = p * q

t = (p - 1)*(q - 1)

# choosen
e = 3
d = [i for i in range(t) if (e * i - 1) % t == 0][0]

print(d)

chars = [4, 15, 7] # number in alphabet
s = 'dog'

print(f"{n=}")
print(f"z={t}")

print(f"Char    M1   {'m**e':<10}  cipher    {'c**d':<14}   M2   out")
for i, c in enumerate(s):
    me = chars[i] ** e
    cd = (me % n) ** d
    print(f"{c}       {chars[i]:<2}   {me:<15} {me % n:<3} ", end="")
    print(f"  {cd:<15}   {cd % n:<3} {s[chars.index(cd % n)]}")
    # locate index of chars in relation index of string dog




print("\n\n")
# ==================================================================
# part b
# ==================================================================


def primes(upperRange):
    def isPrime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    return [i for i in range(upperRange) if isPrime(i)]

def coprime(value, initial=2):
    # returns first instance of a coprime

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    c = initial
    while not gcd(c, value) == 1:
        c += 1
    return c


m = 4583
# need n > m
p, q = 0, 0
# z = (p-1) * (q-1)

prime = primes(300)
prod = {}
lst = []
for dp in prime:
    for dq in prime:
        prod[dq * dp] = [dq, dp]
        if (dp * dq) not in lst:
            lst.append(dp * dq)
lst.sort()

# locate first instance of p * q that's greater than m
for l in lst:
    if l > m:
        p, q = prod[l]
        break

n = p * q
z = (p -1 ) * (q - 1)
e = coprime(z, initial=15) # or set if given
d = [i for i in range(z) if (e * i - 1) % z == 0][0]

ciphertext = m ** e % n
dCiphertext = ciphertext ** d % n

print(f"given {m=}")
print(f"Calculated (p, q) = ({p}, {q})")
print(f"{z=}")
print(f"Calculated (e, d): ({e}, {d})")
print(f"\nEncoded Ciphertext m**e mod n: {ciphertext}")
print(f"Decoded Ciphertext c**d mod n: {dCiphertext}")



