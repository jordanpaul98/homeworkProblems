

def problem3d1():

    from math import log as ln, exp, sqrt
    from bisection import Bisection
    import matplotlib.pyplot as plt

    '''
    problem 3.1
    (a) for a device with Na = 10 ^ 18, tox = 2.5nm, Vfb = -0.8v, plot Ys vs Vgb, with
        Vgb between 0.5 and 2.5v and for Vcb = [0.4, 0.8, 1.2]V, Show approximately the three regions of inversion
        on each curve. Assume that Vhb ~= Vmb + 0.45V
        

    (b) for the same device, plot Ys vs Vcb, with Vcb between 0 and 2.5v for Vgb = [1, 1.5, 2]V
    
    3.2.21
    Vgb = Vfb + Ys + y * sqrt(Ys + Ot * e ^ (Ys - (2 * Of + Vcb))/Ot)
    
    from 3.2.21
    Vcb = Ys - 2Of - Ot * ln( ( (Vgb - Vfb - Ys) ^ 2 / y^2) / Ot )

    '''

    psi = '\u03C8'
    phi = '\u00D8'

    Na = 10 ** 18
    tox = 2.5 * 10 ** -7
    Vfb = -0.8

    kox = 3.9

    def between(Range: list, resolution=100):
        return [Range[0] + r * (Range[1] - Range[0]) / resolution for r in range(resolution + 1)]

    def yNearx(X, Y, findx):
        for x, y in zip(X, Y):
            if x > findx:
                return y

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

    '''
    for part a and b will need Of (fermi potential), -> need ni
    Ot (thermal voltage),
    y (body effect coefficient) -> need Cox -> need Eox -> need Kox
    '''

    ot = Ot(300)
    ofp = Ofp(ot, Na, Ni(300))
    y = Y(Na, Cox(Eox(kox), tox))

    phi_z = [0, 0, 0]

    def Vmb(Vfb, Vcb, Of, y):
        return Vfb + (2 * Of + Vcb) + y * sqrt(2 * Of + Vcb)

    def Vlb(Vfb, Vcb, Of, y):
        return Vfb + (Of + Vcb) + y * sqrt(Of + Vcb)

    def Vgb_3_2_21(Vfb, Ys, y, Ot, Of, Vcb):
        # equation 3.2.21 from textbook to solve for Vgb
        return Vfb + Ys + y * sqrt(Ys + Ot * exp((Ys - (2 * Of + Vcb)) / Ot))

    def part_a():
        Vgb = [0.5, 2.5]
        Vcb = [0.4, 0.8, 1.2]

        vgb = between(Vgb, resolution=1000)
        ys = [[Bisection(lambda x: Vgb_3_2_21(Vfb, x, y, ot, ofp, vcb),
                        Vgb[0] * 0.99, Vgb[1] * 1.01, v) for v in vgb] for vcb in Vcb]

        vlb = [Vlb(Vfb, vcb, ofp, y) for vcb in Vcb] # should approximate to ys = [ofp + vcb for vcb in Vcb]
        vmb = [Vmb(Vfb, vcb, ofp, y) for vcb in Vcb] # should approximate to ys = [2 * ofp + vcb for vcb in Vcb]
        vhb = [_vmb + 0.45 for _vmb in vmb]

        mn_ys = min([min(_ys) for _ys in ys])

        fog, axs = plt.subplots(len(Vcb), 1, figsize=(12, 20))

        for i, _ys in enumerate(ys):
            axs[i].plot(vgb, _ys, label=f"Vcb={Vcb[i]}v")
            axs[i].vlines(vlb[i], mn_ys, yNearx(vgb, _ys, vlb[i]), colors='red', label=f'Vlb = {round(vlb[i], 2)}v')
            axs[i].vlines(vmb[i], mn_ys, yNearx(vgb, _ys, vmb[i]), colors='orange', label=f'Vmb = {round(vmb[i], 2)}v')
            axs[i].vlines(vhb[i], mn_ys, yNearx(vgb, _ys, vhb[i]), colors='yellow', label=f'Vhb = {round(vhb[i], 2)}v')

            axs[i].set_title(f"{psi.upper()}s Vs Vgb  with  Vcb={Vcb[i]}v", fontsize='14')
            axs[i].set_ylabel(f'{psi.upper()}s', fontsize='16')

            axs[i].legend(fontsize='14')

            axs[i].text((Vgb[0] + vlb[i]) / 2, mn_ys, 'Depletion', ha='center')
            axs[i].text((vlb[i] + vmb[i]) / 2, mn_ys, 'Weak', ha='center')
            axs[i].text((vmb[i] + vhb[i]) / 2, mn_ys, 'Moderate', ha='center')
            axs[i].text((vhb[i] + Vgb[-1]) / 2, mn_ys, 'Strong', ha='center')

        axs[-1].set_xlabel("Vgb", fontsize='14')

        plt.show()

    def part_b():

        Vcb = [0, 2.5]
        Vgb = [1, 1.5, 2]

        vcb = between(Vcb, resolution=100)
        ys = [[Bisection(lambda x: Vgb_3_2_21(Vfb, x, y, ot, ofp, v),
                        min(Vcb), max(Vcb), vgb, max_iterations=1000) for v in vcb] for vgb in Vgb]

        fog, axs = plt.subplots(len(Vgb) + 1, 1, figsize=(12, 20))

        for i, _ys in enumerate(ys):
            axs[0].plot(vcb, _ys, label=f"Vgb={Vgb[i]}")

        axs[0].set_title(f"{psi.upper()}s Vs Vcb", fontsize='14')
        axs[0].set_ylabel(f'{psi.upper()}s', fontsize='16')
        axs[0].legend(fontsize='14')

        #axs[0].plot([min(Vcb), xNeary(vcb, ys[-1], )], [2 * ofp, 2 * ofp + 2], 'r--', 'LineWidth', 1)

        def find_of_cross(X, Ys, Of):
            for x, y, z in zip(X, Ys, Of):
                if z > y:
                    return x

        for i, _ys in enumerate(ys, start=1):
            axs[i].plot(vcb, _ys, label=f"Vgb={Vgb[i - 1]}v")

            axs[i].set_title(f"{psi.upper()}s Vs Vcb  with  Vgb={Vgb[i - 1]}v", fontsize='14')
            axs[i].set_ylabel(f'{psi.upper()}s', fontsize='16')

            # Of line Vu(Vgbs)
            of_line_x = [min(Vcb), find_of_cross(vcb, _ys, [v + ofp for v in vcb])]
            of_line_y = [ofp, _ys[vcb.index(of_line_x[-1])]]

            prev_x = of_line_x[-1]

            axs[i].plot(of_line_x, of_line_y, 'o--', label=f"{phi.upper()}f + Vcb")
            axs[i].text(of_line_x[-1] + 0.05, ofp * 1.5, "Vw(Vgs)")
            axs[i].text((max(Vcb) + of_line_x[-1]) / 2, ofp, 'Depletion', ha='center')
            axs[i].vlines(of_line_x[-1], ofp, of_line_y[-1], colors='grey')

            # Of line Vw(Vgbs)
            of_line_x = [min(Vcb), find_of_cross(vcb, _ys, [v + 2 * ofp for v in vcb])]
            of_line_y = [2 * ofp, _ys[vcb.index(of_line_x[-1])]]

            axs[i].plot(of_line_x, of_line_y, 'o--', label=f"2{phi.upper()}f + Vcb")
            axs[i].text(of_line_x[-1] + 0.05, ofp * 1.5, "Vu(Vgs)")
            axs[i].text((prev_x + of_line_x[-1]) / 2, ofp, 'Weak', ha='center')
            axs[i].vlines(of_line_x[-1], ofp, of_line_y[-1], colors='grey')
            axs[i].text(sum(of_line_x) / 2, ofp, 'Strong | Moderate', ha='center')

            axs[i].legend(fontsize='14')

        axs[-1].set_xlabel("Vcb", fontsize='14')

        plt.show()

    part_a()
    part_b()







