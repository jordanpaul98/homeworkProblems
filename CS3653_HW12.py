def Reflective(U, R, out=None):
    # Reflective if: (a, a) E|R m|a-a
    valid = True
    for v in U:
        if not (v, v) in R:
            valid = False
            if out: out(f"     Reflective:   {(v, v)} missing in set")
    return valid


def Symmetric(U, R, out=None):
    # Symmetric if: (a, b) E|R (b, a) ER
    valid = True
    for s in R:
        sr = list(s)
        sr.reverse()
        if not tuple(sr) in [tuple(r) for r in R]:
            valid = False
            if out: out(f"     Symmetric:    {s} reversed: {sr} not in set")
    return valid


def Transitive(U, R, out=None):
    # Transitive if: (a, b) E|R (b, c) then (a, c) E|R
    valid = True
    for s in R:
        for m in [su for su in R if su[0] == s[-1]]:
            find = (s[0], m[-1])
            if not find in [tuple(r) for r in R]:
                if out: out(f"     Transitive:   {s} & {m} not found {find} in set")
                valid = False
    return valid

def AntiSymmetric(U, R):
    valid = True
    for s in R:
        sr = list(s)
        sr.reverse()
        if tuple(sr) in [tuple(r) for r in R] and not sr[0] == sr[1] and sr[0] in U:
            valid = False
    return valid


def CongruenceClass(a, m, s=-3, l=7):
    return [a + i * m for i in range(s, l + s)]

def union(a, b):
    # new set with combined sets
    r = [_a for _a in a]
    for _b in b:
        if not _b in r:
            r.append(_b)
    r.sort()
    return r

def intersection(a, b):
    # same elements in both sets
    return [_a for _a in a if _a in b]


def equivalenceRelations(U, R):
    print("Is Reflective" if Reflective(U, R) else "Not Reflective")
    print("Is Symmetric" if Symmetric(U, R) else "Not Symmetric")
    print("Is Transitive" if Transitive(U, R) else "Not Transitive")

def PartialOrdering(U, R):
    print("Is Reflective" if Reflective(U, R) else "Not Reflective")
    print("Is Antisymmetric" if AntiSymmetric(U, R) else "Not Antisymmetric")
    print("Is Transitive" if Transitive(U, R) else "Not Transitive")
def problem_1():
    """
    Which of these relations on {0, 1, 2, 3} are equivalence relations?
    Determine the properties of an equivalence relation that the others lack.
    a) {(0, 0), (1, 1), (2, 2), (3, 3)}
    b) {(0, 0), (0, 2), (2, 0), (2, 2), (2, 3), (3, 2), (3, 3)}
    c) {(0, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}
    d) {(0, 0), (1, 1), (1, 3), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
    e) {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (3, 3)}
    """

    universe = (0, 1, 2, 3)
    a = [(v, v) for v in range(4)]
    b = [(0, 0), (0, 2), (2, 0), (2, 2), (2, 3), (3, 2), (3, 3)]
    c = [(0, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 3)]
    d = [(0, 0), (1, 1), (1, 3), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    e = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (3, 3)]

    equivalenceRelations(universe, a, print)
    print("")
    equivalenceRelations(universe, b, print)
    print("")
    equivalenceRelations(universe, c, print)
    print("")
    equivalenceRelations(universe, d, print)
    print("")
    equivalenceRelations(universe, e, print)

def problem_2():
    """
    Determine whether relations given by zero–one matrix are equivalence relations:
    a)  1 1 1
        0 1 1   -> (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)
        1 1 1
    """

    universe = (0, 1, 2)
    a = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    equivalenceRelations(universe, a); print("")

    """
    b)  1 0 1 0
        0 1 0 1   -> (0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (3, 1), (3, 3)
        1 0 1 0
        0 1 0 1
    """

    universe = (0, 1, 2, 3)
    b = [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (3, 1), (3, 3)]
    equivalenceRelations(universe, b); print("")

    """
    c)  1 1 1 0
        1 1 1 0   -> (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 3)
        1 1 1 0
        0 0 0 1
    """

    universe = (0, 1, 2, 3)
    c = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 3)]
    equivalenceRelations(universe, c); print("")

def problem_5():

    n, m = 1, 2
    print(CongruenceClass(n, m, -2, 5))

    n, m = 2, 3
    print(CongruenceClass(n, m, -2, 5))

    n, m = 3, 5
    print(CongruenceClass(n, m, -2, 5))

    n, m = 4, 6
    print(CongruenceClass(n, m, -2, 5))

    n, m = 5, 8
    print(CongruenceClass(n, m, -2, 5))

def problem_6():
    """
    Which of these collections of subsets are partitions of {−3, −2, −1, 0, 1, 2, 3}?
    """

    P = [-3, -2, -1, 0, 1, 2, 3]

    def check(a):
        if (union(a[0], a[1]) == P and intersection(a[0], a[1]) == []):
            print("Is partition")
        else:
            print("Is not Partition")

    check([(-3, -1, 1, 3), (-2, 0, 2)])
    check([(-3, -2, -1, 0), (0, 1, 2, 3)])
    # check([(-3, 3), (-2, 2), (-1, 1), (0)]) Is Partition
    check([(-3, -2, 2, 3), (-1, 1)])

def problem_8():
    """
    Which of these relations on {0, 1, 2, 3} are partial orderings?
    Determine the properties of a partial ordering that the others lack.
    a) {(0, 0), (2, 2), (3, 3)}
    b) {(0, 0), (1, 1), (2, 0), (2, 2), (2, 3), (3, 3)}
    c) {(0, 0), (1, 1), (1, 2), (2, 2), (3, 1), (3, 3)}
    d) {(0, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (2, 3), (3, 0), (3, 3)}
    e) {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)}
    """

    universe = (0, 1, 2, 3)
    a = [(0, 0), (2, 2), (3, 3)]
    b = [(0, 0), (1, 1), (2, 0), (2, 2), (2, 3), (3, 3)]
    c = [(0, 0), (1, 1), (1, 2), (2, 2), (3, 1), (3, 3)]
    d = [(0, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (2, 3), (3, 0), (3, 3)]
    e = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)]

    PartialOrdering(universe, a); print("")
    PartialOrdering(universe, b); print("")
    PartialOrdering(universe, c); print("")
    PartialOrdering(universe, d); print("")
    PartialOrdering(universe, e); print("")

#problem_1()
#problem_2()
#problem_5()
#problem_6()
#problem_8()

#a, b, c, d = 0, 1, 2, 3
#equivalenceRelations((a, b, c, d), [(a, a), (a, b), (a, d), (b, b), (b, a), (b, c), (c, c), (c, b), (c, d), (d, d), (d, c), (d, a)])

'''print(AntiSymmetric((1, 2, 3, 4), [(1, 1), (1, 2), (2, 1), (2, 2), (3, 4), (4, 1), (4, 4)]))
print(AntiSymmetric((1, 2, 3, 4), [(1, 1), (1, 3), (3, 1)]))
print(AntiSymmetric((1, 2, 3, 4), [(1, 1), (1, 2), (1, 4), (2, 1), (2, 2), (3, 3), (4, 1), (4, 4)]))
print(AntiSymmetric((1, 2, 3, 4), [(1, 1), (2, 2), (3, 3), (4, 4)]))
'''
