(a) Using RSA, choose p = 3 and q = 11, and encode the word “dog” by encrypting each letter separately.
 Apply the decryption algorithm to the encrypted version to recover the original plaintext message.

(b) Repeat part (a) but now encrypt “dog” as one message m.

dog - > [d, o, g] -> [4, 15, 7] -> [00100, 01111, 00111]
convert dog to 5 bit binary (26 letters in alphabet)










n=33
z=20

Char    M1   m**e        cipher    c**d             M2   out

d       4    64              31    27512614111       4   d

o       15   3375            9     4782969           15  o

g       7    343             13    62748517          7   g



given m=4583

Calculated (p, q) = (43, 107)

z=4452

Calculated (e, d): (17, 2357)

Encoded Ciphertext m**e mod n: 4310

Decoded Ciphertext c**d mod n: 4583

Process finished with exit code 0
