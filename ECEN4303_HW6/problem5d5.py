from math import sqrt

def Problem5d5():

    """

    (a) consider a device with uCox = 500uA/V^2, a=1.1, Ec=2.5*10**4V/cm, and Vt=0.4v
        using the model on example 5.1, plot Ids vs Vds for Vds up to 1.2v
        with Vgs as a parameter (Vgs=0.6, 0.9, 1.2) and W = L = 0.8, 0.4, 0.2 um

    (b) repeat for the preceding values of L, but keep W constant at 0.8um. Discuss the results
        obtained, Neglect the effect of channel length and width on the threshold voltage

    Example 1. (5.2.11)

    Ids = (W / L) * (uCox[(Vgs - Vt) * Vds - 0.5 * a * Vds ** 2] / (1 + Vds/(L * Ec))
    for Vds <= V'ds

    V'ds = (Vgs - Vt) / a * 2 / (1 + sqrt(1 + ((Vgs - Vt) / a) * 2 / (L * Ec))

    """

    from Functions import between
    import matplotlib.pyplot as plt

    uCox = 500 * 10 ** -6
    Ec = 2.5 * 10 ** 4
    Vt = 0.4
    a = 1.1

    Vds = between((0, 1.2), resolution=100)
    Vgs = [0.6, 0.9, 1.2]


    def Ids(W, L, Vgs, Vds):
        # Page 248 5.2.11
        return (W / L) * uCox * ((Vgs - Vt) * Vds - 0.5 * a * Vds ** 2) / (1 + Vds / (L * Ec))

    def Vdsp(Vgs, L):
        # Page 248 5.2.12
        return ((Vgs - Vt) / a) * (2 / (1 + sqrt(1 + ((Vgs - Vt) / a) * (2 / (L * Ec)))))

    fog, axis = plt.subplots(len(Vgs), 1, figsize=(12, 16))

    for i, WL in enumerate([0.8, 0.4, 0.2]):

        W = L = WL * 10 ** -4

        for vgs in Vgs:

            vdsp = Vdsp(vgs, L)

            ids = []
            for vds in Vds:
                if vds <= vdsp:
                    ids.append(Ids(W, L, vgs, vds))
                else:
                    ids.append(ids[-1] if ids else 0)

            axis[i].plot(Vds, ids, label=f"Vgs={vgs}")

        axis[i].set_title(f"Ids vs Vds    W=L={WL}um", fontsize=16)
        axis[i].set_ylabel("Ids", fontsize=16)
        axis[i].legend()

    axis[-1].set_xlabel("Vds", fontsize=16)

    plt.show()

    # ======================================================================================
    #  part b
    # ======================================================================================

    fog, axis = plt.subplots(len(Vgs), 1, figsize=(12, 16))

    W = 0.8 * 10 ** -4
    for i, WL in enumerate([0.8, 0.4, 0.2]):

        L = WL * 10 ** -4

        for vgs in Vgs:

            vdsp = Vdsp(vgs, L)

            ids = []
            for vds in Vds:
                if vds <= vdsp:
                    ids.append(Ids(W, L, vgs, vds))
                else:
                    ids.append(ids[-1] if ids else 0)

            axis[i].plot(Vds, ids, label=f"Vgs={vgs}")

        axis[i].set_title(f"Ids vs Vds    W=0.8, L={WL}um", fontsize=16)
        axis[i].set_ylabel("Ids", fontsize=16)
        axis[i].legend()

    axis[-1].set_xlabel("Vds", fontsize=16)

    plt.show()


