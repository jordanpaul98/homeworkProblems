

def Problem4d14():

    """

    for the transistor in prob 4.1, assume Vsb = 0v and plot Ids vs Vds for Vgs = 1 and Vgs = 1.5
    using (a) (4.7.11) with 4.7.2 and (b) (4.7.24), first using alpha from (4.7.27),
    and then modifying the value of alpha to improve accuracy

    first part of the problem will use function: Idsn_a

    phi_so ~= phi_0 + Vsb  (4.7.1a)
    phi_sl ~= phi_0 + Vdb  (4.7.1b)

    Ids = {Idsn, Vdb <= Vp

    Vp -> (4.7.9) (pinchoff voltage)
    Vp = (-gamma / 2 + sqrt(gamma ** 2 / 4 + Vgb - Vfb)) ** 2 - phi_0

    Vp ~= Vdb

    Ids = (W/L)*mu*Cox*((Vgs - Vt)*Vds - (alpha ** 2 / 2) * Vds **2  (4.7.24a) page 194
    (4.7.27)  alpha = 1 + gamma / ( 2 * sqrt(phi_0 + Vsb)) page 199

    Vt = Vto + gamma * (sqrt(phi_0 + Vsb) - sqrt(phi_0))  (4.7.20a) page 194
    also Vt = Vfb + phi_0 + gamma * sqrt(phi_0 + Vsb)     (4.7.19)  page 193
    vto = Vfb + phi_0 + gamma * sqrt(phi_0)               (4.7.20b) page 194


    foot note: Page 187
    Vdb = Vds + Vsb
    Vgb = Vgs + Vsb

    """

    from math import sqrt, exp, log as ln
    import matplotlib.pyplot as plt

    # ====================================================================================
    # Functions     Functions     Functions     Functions     Functions     Functions
    # ====================================================================================

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

    def between(Range: list, resolution=100):
        return [Range[0] + r * (Range[1] - Range[0]) / resolution for r in range(resolution + 1)]

    # ====================================================================================
    # Setup     Setup     Setup     Setup     Setup     Setup     Setup     Setup
    # ====================================================================================

    Na = 5 * 10 ** 17
    tox = 2 * 10 ** -9
    Vfb = -0.75
    u = 400
    W = 1 * 10 ** -4
    L = 0.1 * 10 ** -4
    Vsb = 0
    Vdb = 1.5
    Vgb = [1, 1.5]

    vds = between([0, 1.5], 1000)

    phi_t = Ot(300)
    phi_f = Ofp(phi_t, Na, Ni(300))
    cox = Cox(Eox(3.9), tox * 100)
    gamma = Y(Na, cox)


    # ====================================================================================
    # Part A     Part A     Part A     Part A     Part A     Part A     Part A     Part A
    # ====================================================================================

    def Vp(gamma, vgb, vfb, phi_0):
        # (4.7.9)
        return (-gamma / 2 + sqrt(gamma ** 2 / 4 + vgb - vfb)) ** 2 - phi_0

    def Phi_0(phi_f, thermal_voltage, n=6):
        """
        2.6.2 from note section on page 186
        """
        return 2 * phi_f + n * thermal_voltage

    def Idsn_a(W, L, mu, cox, vgb, vfb, vdb, vsb, phi_0, gamma):
        """
        for first part of the problem
        4.7.2a Page 186
        """

        outer = (W / L) * mu * cox
        inner = (vgb - vfb)*(vdb - vsb)
        inner += - 0.5 * ((phi_0 + vdb) ** 2 - (phi_0 + vsb) ** 2)
        inner += -(2/3) * gamma * ((phi_0 + vdb) ** (3/2) - (phi_0 + vsb) ** (3/2))

        return outer * inner

    def Idsn_b(W, L, mu, cox, vgb, vfb, phi_0, vdb, vsb, gamma):
        """
        4.7.2b page 187
        """

        outer = (W / L) * mu * cox
        inner = (vgb - vfb - phi_0) * (vdb - vsb)
        inner += -0.5 * (vdb ** 2 - vsb ** 2)
        inner += -(2/3) * gamma * ((phi_0 + vdb) ** (3/2) - (phi_0 + vsb) ** (3/2))

        return outer * inner

    phi_0 = Phi_0(phi_f, phi_t)
    full_ids = {}

    for vgb in Vgb:

        vp = Vp(gamma, vgb, Vfb, phi_0)

        ids = []
        Idsn_dw_x = []
        Idsn_dw_y = []

        full_ids[vgb] = []

        for v in vds:
            if v <= vp: # Vdn <= Vp
                ids.append( Idsn_a(W, L, u, cox, vgb, Vfb, v, Vsb, phi_0, gamma) )
            else: # Vdn > Vp
                # Ids' in saturation
                ids.append(ids[-1])

                #for marking out Idsn after Vp
                Idsn_dw_y.append(Idsn_a(W, L, u, cox, vgb, Vfb, v, Vsb, phi_0, gamma))
                Idsn_dw_x.append(v)

            full_ids[vgb].append(ids[-1])

        Idsn_dw_x = Idsn_dw_x[:int(.3 * len(Idsn_dw_x))]
        Idsn_dw_y = Idsn_dw_y[:int(.3 * len(Idsn_dw_y))]

        ix = min(Idsn_dw_x) + (max(Idsn_dw_x) - min(Idsn_dw_x)) / 2
        iy = min(Idsn_dw_y) + (max(Idsn_dw_y) - min(Idsn_dw_y)) / 2

        plt.text(ix, iy, "Idsn", ha='center', va='top', fontsize=11)

        plt.vlines(vp, min(ids), max(ids), color='grey', linestyles='--')
        plt.hlines(max(Idsn_dw_y), 0, vp, color='grey', linestyles='--')
        plt.text(vp, min(ids) - 0.00005, 'Vp', ha='center', va='top', fontsize=13)
        plt.text(0, max(Idsn_dw_y), "I'ds", ha='right', va='center', fontsize=13)

        plt.plot(vds, ids, label=f"Vgb={vgb}", linewidth=3)
        plt.plot(Idsn_dw_x, Idsn_dw_y, "r--")

    plt.title("Part (a) --  Ids vs. Vds using 4.7.11 with 4.7.2")
    plt.ylabel("Ids(A)", fontsize=14)
    plt.xlabel("Vds", fontsize=14)
    plt.legend(loc='lower right')
    plt.show()

    # ====================================================================================
    # Part B     Part B     Part B     Part B     Part B     Part B     Part B     Part B
    # ====================================================================================

    def Alpha(gamma, phi_0, vsb):
        return 1 + gamma / (2 * sqrt(phi_0 + vsb))

    def Ids_a(W, L, mu, cox, vgs, vt, vds, alpha):
        '''
        4.7.24a page 194

        for Vds <= Vds'
        '''
        return (W / L) * mu * cox * ((vgs - vt) * vds - (alpha / 2)* vds ** 2)

    def Ids_b(W, L, mu, cox, vgs, vt, alpha):
        """
        2.7.24b page 194

        for Vds > Vds'
        """

        return (W / L) * mu * cox * ((vgs - vt) ** 2) / (2 * alpha)

    def Vt(vto, gamma, phi_0, vsb):
        """
        4.7.20a Page 194
        """

        return vto + gamma * (sqrt(phi_0 + vsb) - sqrt(phi_0))

    def Vto(vfb, phi_0, gamma):
        """
        4.7.20b Page 194
        """

        return vfb + phi_0 + gamma * sqrt(phi_0)

    def Vdsp(vgs, vt, alpha):
        """
        Vds prime
        4.7.21 Page 194
        """

        return (vgs - vt) / alpha

    alpha = Alpha(gamma, phi_0, Vsb)

    vto = Vto(Vfb, phi_0, gamma)
    vt = Vt(vto, gamma, phi_0, Vsb)

    alpha_char = '\u03B1'

    for vgb in Vgb:

        vdsp = Vdsp(vgb, vt, alpha) # Vds' prime

        print(vdsp)

        ids = []
        Idsn_dw_x = []
        Idsn_dw_y = []
        for v in vds:
            if v <= vdsp: # Vds <= Vds'
                ids.append( Ids_a(W, L, u, cox, vgb, vt, v, alpha) )
            else:
                ids.append( Ids_b(W, L, u, cox, vgb, vt, alpha) )

                # for marketing out Ids curve beyond Vds'
                Idsn_dw_x.append(v)
                Idsn_dw_y.append(Ids_a(W, L, u, cox, vgb, vt, v, alpha))


        Idsn_dw_x = Idsn_dw_x[:int(.3 * len(Idsn_dw_x))]
        Idsn_dw_y = Idsn_dw_y[:int(.3 * len(Idsn_dw_y))]

        ix = min(Idsn_dw_x) + (max(Idsn_dw_x) - min(Idsn_dw_x)) / 2
        iy = min(Idsn_dw_y) + (max(Idsn_dw_y) - min(Idsn_dw_y)) / 2

        plt.text(ix, iy, "Idsn", ha='center', va='top', fontsize=11)

        plt.vlines(vdsp, min(ids), max(ids), color='grey', linestyles='--')
        plt.hlines(max(Idsn_dw_y), 0, vdsp, color='grey', linestyles='--')
        plt.text(vdsp, min(ids) - 0.00005, "V'ds", ha='center', va='top', fontsize=13)
        plt.text(0, max(Idsn_dw_y), "I'ds", ha='right', va='center', fontsize=13)

        #plt.plot(vds, full_ids, label='ids curve')
        plt.plot(vds, ids, label=f"Vgb={vgb:.1f} & {alpha_char}={alpha:.3f}", linewidth=3)
        plt.plot(Idsn_dw_x, Idsn_dw_y, "r--")

    plt.title(f"Part (b) --  Ids vs. Vds using 4.7.24 with {alpha_char} from 4.7.27")
    plt.ylabel("Ids(A)", fontsize=14)
    plt.xlabel("Vds", fontsize=14)
    plt.legend(loc='lower right')
    plt.show()

    # =======================================================================================
    # Improve Alpha     Improve Alpha     Improve Alpha     Improve Alpha     Improve Alpha
    # =======================================================================================

    def Vdsp_reversed(vdsp, vgs, vt):
        """
        will use the Vdsp equation to calculate alpha from max point to obtain Vds before saturation with equation 4.7.2
        """

        return (vgs - vt) / vdsp

    calculate_error = {}
    improved_error = {}

    for vgb in Vgb:

        # from part A using list full_ids, will find the max point and match to vds

        vdsp = Vdsp(vgb, vt, alpha)  # Vds' prime

        vds_max = vds[full_ids[vgb].index(max(full_ids[vgb]))]

        print(f"Vds before saturation: {vds_max}")
        print(f"Vds' calculated from alpha: {vdsp} w/ {alpha=}")

        improved_alpha = Vdsp_reversed(vds_max, vgb, vt)

        vdsp = Vdsp(vgb, vt, improved_alpha) # Vds' prime

        ids = []
        ids_cal_alpha = []
        Idsn_dw_x = []
        Idsn_dw_y = []
        for v in vds:
            if v <= vdsp: # Vds <= Vds'
                ids.append( Ids_a(W, L, u, cox, vgb, vt, v, improved_alpha) )
                ids_cal_alpha.append( Ids_a(W, L, u, cox, vgb, vt, v, alpha) )
            else:
                ids.append( Ids_b(W, L, u, cox, vgb, vt, improved_alpha) )
                ids_cal_alpha.append( Ids_b(W, L, u, cox, vgb, vt, improved_alpha) )

                # for marketing out Ids curve beyond Vds'
                Idsn_dw_x.append(v)
                Idsn_dw_y.append(Ids_a(W, L, u, cox, vgb, vt, v, improved_alpha))

        Idsn_dw_x = Idsn_dw_x[:int(.3 * len(Idsn_dw_x))]
        Idsn_dw_y = Idsn_dw_y[:int(.3 * len(Idsn_dw_y))]

        ix = min(Idsn_dw_x) + (max(Idsn_dw_x) - min(Idsn_dw_x)) / 2
        iy = min(Idsn_dw_y) + (max(Idsn_dw_y) - min(Idsn_dw_y)) / 2

        plt.text(ix, iy, "Idsn", ha='center', va='top', fontsize=11)

        plt.vlines(vdsp, min(ids), max(ids), color='grey', linestyles='--')
        plt.hlines(max(Idsn_dw_y), 0, vdsp, color='grey', linestyles='--')
        plt.text(vdsp, min(ids) - 0.00005, "V'ds", ha='center', va='top', fontsize=13)
        plt.text(0, max(Idsn_dw_y), "I'ds", ha='right', va='center', fontsize=13)

        #plt.plot(vds, full_ids, label='ids curve')
        plt.plot(vds, full_ids[vgb], color='grey', label=f"Vgb={vgb:.1f}  Original")
        plt.plot(vds, ids, label=f"Vgb={vgb:.1f} & improved: {alpha_char}={improved_alpha:.3f}", linewidth=3)
        plt.plot(Idsn_dw_x, Idsn_dw_y, "r--")

        calculate_error[vgb] = [100 * abs((e_ids - g_ids)/e_ids if e_ids > 0 else 0) for e_ids, g_ids in zip(full_ids[vgb], ids_cal_alpha)]
        improved_error[vgb] = [100 * abs((e_ids - g_ids)/e_ids if e_ids > 0 else 0) for e_ids, g_ids in zip(full_ids[vgb], ids)]

    plt.title(f"Modify Alpha --  Ids vs. Vds using 4.7.24 with {alpha_char} from 4.7.27")
    plt.ylabel("Ids(A)", fontsize=14)
    plt.xlabel("Vds", fontsize=14)
    plt.legend(loc='lower right')
    plt.show()


    plt.title(f"Absolute Error using calculated {alpha_char} Vs the modified {alpha_char}", fontsize=13)

    for vgb, error in calculate_error.items():
        plt.plot(vds, error, "--", label=f"Vgb={vgb:.1f}: 4.7.27 Calculated {alpha_char}")

    for vgb, error in improved_error.items():
        plt.plot(vds, error, label=f"Vgb={vgb:.1f}: Improved Alpha", linewidth=3)

    plt.xlabel("Vds", fontsize=14)
    plt.ylabel("Abs( % error)", fontsize=14)
    plt.legend(fontsize=13)
    plt.show()











































