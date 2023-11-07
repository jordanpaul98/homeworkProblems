

def problem4d1():

    from math import log as ln, exp, sqrt
    from bisection import Bisection
    import matplotlib.pyplot as plt

    from Functions import Ot, Ni, Ofp, Eox, Cox, Y, between

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

    vgb = between([0, 1.5], resolution=100)

    def Vgb(flatband_volt, phi, gamma, thermal_volt, fermi_volt, voltage_to_base):
        """
        4.3.15
        :param voltage_to_base: any form of Vcb, Vsb, Vdb...
        :return:
        """

        return phi + flatband_volt + gamma * sqrt(phi + thermal_volt * exp((phi - 2 * fermi_volt - voltage_to_base) / thermal_volt))

    ot = Ot(300)
    ofp = Ofp(ot, Na, Ni(300))
    cox = Cox(Eox(kox), tox)
    y = Y(Na, cox)

    def Ids1(gate_voltage, flatband_volt, W, L, mu, oxide, phi_sl, phi_so, gamma):
        #drift current

        return (W / L) * mu * oxide * \
               ((voltage_gate - flatband_volt) * (phi_sl - phi_so) - 0.5 * (phi_sl ** 2 - phi_so ** 2) - (2/3) * gamma * (phi_sl ** (3/2) - phi_so ** (3/2)))

        # 4.3.14a
        '''A = Cox * u * W / L
        B = (Vgb - Vfb) * (Ysl - Ys0)
        C = (1/2) * (Ysl ** 2 - Ys0 ** 2)
        D = (2/3) * (Ysl ** (3/2) - Ys0 ** (3/2))
        return A * (B - C - D)'''

    def Ids2(W, L, mu, oxide, thermal_volt, phi_sl, phi_so, gamma):
        #diffusion current
        # 4.3.14b

        return (W / L) * mu * oxide * (thermal_volt * (phi_sl - phi_so) + thermal_volt * gamma * (phi_sl ** (1/2) - phi_so ** (1/2)))

        A = oxide * mu * W / L
        B = thermal_volt * (phi_sl - phi_so)
        C = thermal_volt * gamma * (phi_sl ** 0.5 - phi_so ** 0.5)
        return A * (B + C)

    def Ids(W, L, mu, oxide, thermal_volt, gate_voltage, flatband_volt, phi_sl, phi_so, gamma):

        outside = (W / L) * mu * oxide
        inside = voltage_gate - flatband_volt - 0.5 * (phi_sl + phi_so)
        inside = inside - (2/3) * gamma * ((phi_sl + phi_sl ** (1/2) * phi_so ** (1/2) + phi_so)/(phi_sl ** 0.5 + phi_so ** 0.5))
        inside = inside + thermal_volt * (1 + gamma / (phi_sl ** 0.5 + phi_so ** 0.5))

        return outside * inside * (phi_sl - phi_so)

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

    ids1 = []
    ids2 = []
    ids = []
    for voltage_gate, so, sl in zip(vgb, yso, ysl):
        ids1.append(abs(Ids1(voltage_gate, Vfb, W, L, u, cox, sl, so, y)))
        ids2.append(abs(Ids2(W, L, u, cox, ot, sl, so, y)))
        ids.append(abs(Ids(W, L, u, cox, ot, voltage_gate, Vfb, sl, so, y)))

    plt.plot(vgb, ids1, label='drift current')
    plt.plot(vgb, ids2, label='diffusion current')
    plt.plot(vgb, ids, label='Ids')
    plt.yscale('log')
    plt.xlim(0.4, 1.6)
    #plt.ylim(1e-8, 1e-2)

    plt.ylabel("Log(IDS)")
    plt.xlabel("Vgb")

    plt.legend(fontsize='14')
    plt.show()























