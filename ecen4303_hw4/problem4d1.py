

def problem4d1():

    from math import log as ln, exp, sqrt
    from bisection import Bisection
    import matplotlib.pyplot as plt

    '''
    
    problem 4.1
    Plot the total drain current, the component due to drift, and the component due to diffusion, using relations from sec. 4.3,
    for a n-channel transistor with Na=5 * 10 ^ 17, tox=2nm, Vfb = -0.75, u = 400, w=1um, l=0.1 um, bias with Vsb = 0.5v, Vdb = 1.5v
    for Vgb between 0, 1.5v
    
    use a log current axis. identify the three regions of inversion
    
    '''

    Na = 5 * 10 ** 17
    tox = 2 * 10 ** -7
    Vfb = -0.75
    u = 400
    W = 1 * 10 ** -4
    L = 0.1 * 10 ** -4
    Vsb = 0.5
    Vdb = 1.5
    kox = 3.9

    def between(Range: list, resolution=100):
        return [Range[0] + r * (Range[1] - Range[0]) / resolution for r in range(resolution + 1)]

    vgb = between([0, 1.5], resolution=100)

    def Ot(T) -> float:
        """ thermal voltage page 9
            @ 300 K Ot = ~25.9mV
            :param T: temperature in kelvin 300 for room temp
            :return: thermal voltage     """
        k = 1.3807 * 10 ** -23  # page 8 Boltzmann constant
        q = 1.602 * 10 ** -19  # page 3 Charge

        thermal_voltage = k * T / q
        print(f"Thermal Voltage: Ot= {thermal_voltage}")

        return thermal_voltage

    def Ni(t) -> float:
        ''' Approximate formula for ni in a semiconductor by temperature page 4
            :param t: temperature
            :return: ni     '''
        A1, A2 = 7 * 10 ** 15, 6600  # given constants

        ni = A1 * (t ** (3.0 / 2.0)) * exp(-A2 / t)

        print(f"ni approximate: ni= {ni:.3e}")

        return ni

    def Ofp(Ot, Na, ni) -> float:
        """ p-type material fermi potential     #page 9
            NOTE: NA or ND with concentration of 10**20 is approx to 0.56 or -0.56 in the book
        :param Ot: Thermal Voltage
        :param Na:  substrate concentration
        :param ni: substrate ni
        :return: fermi potential
        """

        ofp = Ot * ln(Na / ni)

        print(f"P-type Fermi Potential: Ofn= {ofp}")

        return ofp

    def Eox(Kox) -> float:
        """ permittivity   #page 70
        :param Kox: dielectric constant
        :return:
        """
        eo = 8.854 * 10 ** -14  # permittivity of free space
        return Kox * eo

    def Cox(Eox, tox) -> float:
        """ oxide capacitance       #page 70
        :param Eox: permittivity
        :param tox: thickness
        :return:
        """
        return Eox / tox

    def Y(Na, Cox):
        """
        Body Effect Coefficient
        :param Na: Acceptor concentration
        :param Cox: oxide capacitance
        :return: y
        """

        q = 1.602 * 10 ** -19  # charge
        Es = 1.05 * 10 ** -12  # permittivity of silicon

        y = sqrt(2 * q * Es * Na) / Cox

        return y

    def Vgb(Vfb, Ys, y, Ot, Of, V_b):
        """
        4.3.15
        :param V_b: any form of Vcb, Vsb, Vdb...
        :return:
        """

        return Ys + Vfb + y * sqrt(Ys + Ot * exp((Ys - 2 * Of - V_b) / Ot))

    ot = Ot(300)
    ofp = Ofp(ot, Na, Ni(300))
    cox = Cox(Eox(kox), tox)
    y = Y(Na, cox)

    def Ids1(Vgb, Vfb, W, L, u, Cox, Ysl, Ys0, y):
        #drift current
        # 4.3.14a
        A = Cox * u * W / L
        B = (Vgb - Vfb) * (Ysl - Ys0)
        C = (1/2) * (Ysl ** 2 - Ys0 ** 2)
        D = (2/3) * (Ysl ** (3/2) - Ys0 ** (3/2))
        return A * (B - C - D)

    def Ids2(W, L, u, Cox, Ot, Ysl, Ys0, y):
        #diffusion current
        # 4.3.14b
        A = Cox * u * W / L
        B = Ot * (Ysl - Ys0)
        C = Ot * y * (Ysl ** 0.5 - Ys0 ** 0.5)
        return A * (B + C)

    def functionA(x):
        # Ysl is found using Vdb
        return Vgb(Vfb, x, y, ot, ofp, Vdb)

    def functionB(x):
        # Ys0 is found using Vsb
        return Vgb(Vfb, x, y, ot, ofp, Vsb)

    ysl = []
    yso = []
    for gate_voltage in vgb:
        yso.append(Bisection(functionB, min(vgb), max(vgb) + 0.5, gate_voltage, tolerance=1e-10, max_iterations=10000))
        ysl.append(Bisection(functionA, min(vgb), max(vgb) + 0.5, gate_voltage, tolerance=1e-10, max_iterations=10000))

        print(f"Looking for gate voltage: {gate_voltage}   with ys0={round(yso[-1], 4)}: got {functionB(yso[-1])}")
        print(f"Looking for gate voltage: {gate_voltage}   with ysl={round(ysl[-1], 4)}: got {functionA(ysl[-1])}")
        print("")

    ids1 = []
    ids2 = []
    ids = []
    for voltage_gate, so, sl in zip(vgb, yso, ysl):
        ids1.append(abs(Ids1(voltage_gate, Vfb, W, L, u, cox, sl, so, y)))
        ids2.append(abs(Ids2(W, L, u, cox, ot, sl, so, y)))
        ids.append(ids1[-1] + ids2[-1])

    plt.plot(vgb, ids1, label='drift current')
    plt.plot(vgb, ids2, label='diffusion current')
    plt.plot(vgb, ids, label='Ids')
    plt.yscale('log')
    plt.xlim(0.8, 1.5)
    plt.ylim(1e-8, 1e-2)
    
    plt.ylabel("Log(IDS)")
    plt.xlabel("Vgb")

    plt.legend(fontsize='14')
    plt.show()























