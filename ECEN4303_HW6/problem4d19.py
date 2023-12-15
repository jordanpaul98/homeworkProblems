

def problem4d19():

    from math import log as ln, exp, sqrt
    from bisection import Bisection
    import matplotlib.pyplot as plt

    from Functions import Ot, Ni, Ofp, Eox, Cox, Y, between

    """
    for the device of prob 4.1 in weak inversion, plot (a) Ids vs Vds with Vsb=0
    for Vds between 0 and 0.5v and Vgs values of Vm - 50mv and Vm - 100mv.
    
    Use, 4.8.6 and 4.8.7
    
    (b) log Ids vs Vgs with Vds = 1v, for Vsb = 0v, Vsb = 0.5v
    
    #page 205
    4.8.6 -> Ids = W/L * I'(Vgb)[e ** (-Vsb/Ot) - e ** (-Vdb/Ot)]
    4.8.7 -> I'(Vgb) = u * sqrt(2qEsNa) / (2 * sqrt(Ysa(Vgb))) * Ot ** 2 * e ** [Ysa(Vgb) - 2 * Of]/Ot
    
    need 4.8.2 (Page 204)
    4.8.2 -> Ysa(Vgb) = (-y/2 + sqrt(y**2 / 4 + Vgb - Vfb)) ** 2
    
    4.6.3 -> Vm = Vfb + 2 * Of + y * sqrt(2 * Of + Vsb')
    
    foot note: Page 187
    Vdb = Vds + Vsb
    Vgb = Vgs + Vsb
    
    Vgb = {Vm - 50mV, Vm - 100mV} + Vsb 
    
    """

    Na = 5 * 10 ** 17
    tox = 2 * 10 ** -9
    Vfb = -0.75
    u = 400
    W = 1 * 10 ** -4
    L = 0.1 * 10 ** -4
    Vsb = 0.0
    Vdb = 1.5
    kox = 3.9

    Vds = between((0, 0.5), resolution=100)

    ot = Ot(300)
    ofp = Ofp(ot, Na, Ni(300))
    cox = Cox(Eox(kox), tox * 100)
    y = Y(Na, cox)


    def Ids(W, L, I_Vgs, Vsb, Vdb, Ot):
        # page 205 4.8.6
        # Note I_Vgs come from equation 4.8.7
        return (W / L) * I_Vgs * (exp(-Vsb / Ot) - exp(-Vdb / Ot))

    def IVgs(u, Na, Ysa_Vgb, Ot, Of):
        # page 205 4.8.7
        # Note Ysa_Vgb come from equation 4.8.2
        q = 1.602 * 10 ** -19  # charge
        Es = 1.05 * 10 ** -12  # permittivity of silicon
        return u * sqrt(2 * q * Es * Na) / (2 * sqrt(Ysa_Vgb)) * Ot ** 2 * exp((Ysa_Vgb - 2 * Of) / Ot)

    def YsaVgb(y, Vgb, Vfb):
        # page 204 4.8.2
        return (-y/2 + sqrt(y ** 2 / 4 + Vgb - Vfb)) ** 2

    def Vm(Vfb, Of, y, Vsb):
        # page 183 4.6.3
        return Vfb + 2 * Of + y * sqrt(2 * Of + Vsb)


    Vgs_1 = Vm(Vfb, ofp, y, Vsb) - 50e-3
    Vgs_2 = Vm(Vfb, ofp, y, Vsb) - 100e-3

    print(f"\n{Vgs_1=:.4f}\n{Vgs_2=:.4f}")

    # ======================================================================================
    #  for Vgs = Vm - 50mV
    # ======================================================================================

    # Note see foot note on page 187 for vgb, vds
    vgb = Vgs_1 + Vsb
    ysa_vgb = YsaVgb(y, vgb, Vfb)
    i_vgs = IVgs(u, Na, ysa_vgb, ot, ofp)

    ids = [Ids(W, L, i_vgs, Vsb, (vds + Vsb), ot) for vds in Vds]

    plt.plot(Vds, ids, label='Vgb=Vm-50mV')

    plt.vlines(3 * ot, 0, max(ids), color='grey', linestyles='--')

    # ======================================================================================
    #  for Vgs = Vm - 100mV
    # ======================================================================================

    # Note see foot note on page 187 for vgb, vds
    vgb = Vgs_2 + Vsb
    ysa_vgb = YsaVgb(y, vgb, Vfb)
    i_vgs = IVgs(u, Na, ysa_vgb, ot, ofp)

    ids = [Ids(W, L, i_vgs, Vsb, (vds + Vsb), ot) for vds in Vds]

    plt.plot(Vds, ids, label='Vgb=Vm-100mV')


    phi = '\u00D8'.upper()
    plt.text(3.2 * ot, 0, f"3 * {phi}t")
    plt.title("Ids vs Vds  (problem 4.19(a))")
    plt.ylabel("Ids", fontsize=14)
    plt.xlabel("Vds", fontsize=14)
    plt.legend()
    plt.show()

    # ======================================================================================
    #  part b
    # ======================================================================================

    Vds = 1
    Vgs = between((0, 0.5), resolution=100)

    Vsb = 0.0

    vgb = [vgs + Vsb for vgs in Vgs]
    ysa_vgb = [YsaVgb(y, _vgb, Vfb) for _vgb in vgb]
    i_vgs = [IVgs(u, Na, ysaVgb, ot, ofp) for ysaVgb in ysa_vgb]
    ids = [Ids(W, L, ivgs, Vsb, (Vds + Vsb), ot) for ivgs in i_vgs]

    plt.plot(Vgs, ids, label='Vsb=0v')

    Vsb = 0.5

    vgb = [vgs + Vsb for vgs in Vgs]
    ysa_vgb = [YsaVgb(y, _vgb, Vfb) for _vgb in vgb]
    i_vgs = [IVgs(u, Na, ysaVgb, ot, ofp) for ysaVgb in ysa_vgb]
    ids = [Ids(W, L, ivgs, Vsb, (Vds + Vsb), ot) for ivgs in i_vgs]

    plt.plot(Vgs, ids, label='Vsb=0.5v')
    plt.yscale('log')

    plt.xlabel("Vgs", fontsize=14)
    plt.ylabel("Ids (log)", fontsize=14)
    plt.title("Ids vs Vgs  (Problem 4.19(b)")

    plt.legend()
    plt.show()














