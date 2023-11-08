
"""
Jordan Paul:
Logic Path Delay: Created for homework 5 problem 2 to display logic expression

create and get the path delay from input H
Note: this version only works for balanced non branching circuits as B is expected to be 1

Nand, Nor and inverters.

create a logic circuit by Logic() with any number of series input gates

Ex. 4 input AND gate, is a 4 Input NAND with a Inverter on its output, the logic setup is as follows
logic = Logic(Nand(4), Inverter())

calling logic.delay(1) or any number H will return total path delay D
logic.pathEffort(H) will return the path effort usually noted as F multiplied by H
logic.pathDelay() will return the path delay usually noted as P is the sum of the gates parasitic delay
logic.stages() will return number of stages, Noted as N or can use len(Logic)
print(Logic) will print out Logic Path expression:
  Ex.
  Name (if given):  Stages- (N)   Delay = N * (H * pathEffort()) ^ (1 / N) + pathDelay()

"""

def Problem2PathEffort():

    class Nand():
        def __init__(self, inputs):
            self.inputs = inputs

        def logicalEffort(self):
            return (self.inputs + 2) / 3

        def parasiticDelay(self):
            return self.inputs

    class Nor():
        def __init__(self, inputs):
            self.inputs = inputs

        def logicalEffort(self):
            return (2 * self.inputs + 1) / 3

        def parasiticDelay(self):
            return self.inputs

    class Inverter():
        def __init__(self, *args):
            self.inputs = 1

        def logicalEffort(self):
            return self.inputs

        def parasiticDelay(self):
            return self.inputs

    class Logic():
        def __init__(self, *args, name=''):
            self.gates = args
            self.name = name

        def pathEffort(self, H=1): # F
            for gate in self.gates:
                H *= gate.logicalEffort()
            return H

        def pathDelay(self): # P
            return sum([gate.parasiticDelay() for gate in self.gates])

        def __len__(self): # N
            return len(self.gates)

        def stages(self): # N
            return len(self)

        def delay(self, H=1):
            # D = N * F ^ (1 / N) + P
            return len(self) * self.pathEffort(H) ** (1. / len(self)) + self.pathDelay()

        def __str__(self):
            return f"{self.name}{':  ' if self.name else ''}Stages- {len(self)}" \
                   f"   Delay = {len(self)} * (H * {self.pathEffort():.3f}) ^ (1 / {len(self)}) + {self.pathDelay()}"

    a = Logic(Nand(6), Inverter(), name='a')
    b = Logic(Nand(3), Nor(2), name='b')
    c = Logic(Nand(2), Nor(3), name='c')
    d = Logic(Nand(3), Inverter(), Nand(2), Inverter(), name='d')

    selection = ['a', 'b', 'c', 'd']
    H = [1, 5, 20, 100]

    Da = [round(a.delay(h), 2) for h in H]
    Db = [round(b.delay(h), 2) for h in H]
    Dc = [round(c.delay(h), 2) for h in H]
    Dd = [round(d.delay(h), 2) for h in H]

    print(a); print(b); print(c); print(d)

    print("\n   H=    ", end='')
    print(str(f"|".join(f"     {sel:<5}  " for sel in selection)))
    print("-".join("" for _ in range(60)))

    for h, la, lb, lc, ld in zip(H, Da, Db, Dc, Dd):
        out = [la, lb, lc, ld]
        print(f" {h:<6}||  {la:<8}  |  {lb:<8}  |  {lc:<8}  |  {ld:<8}")

    print()

    for i, (la, lb, lc, ld) in enumerate(zip(Da, Db, Dc, Dd)):
        out = [la, lb, lc, ld]
        print(f"For H={H[i]:<4} best gate={selection[out.index(min(out))]}")

    
    '''
    from slides
    
    sa = Logic(Nand(8), Inverter())
    sb = Logic(Nand(4), Nor(2))
    sc = Logic(Nand(2), Nor(2), Nand(2), Inverter())

    print(sa)
    print(sb)
    print(sc)

    print(sa.delay(1), sa.delay(12))
    print(sb.delay(1), sb.delay(12))
    print(sc.delay(1), sc.delay(12))'''





