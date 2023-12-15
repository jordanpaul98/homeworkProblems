
======================================================================================================
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
======================================================================================================

    (a) consider a device with uCox = 500uA/V^2, a=1.1, Ec=2.5*10**4V/cm, and Vt=0.4v
        using the model on example 5.1, plot Ids vs Vds for Vds up to 1.2v
        with Vgs as a parameter (Vgs=0.6, 0.9, 1.2) and W = L = 0.8, 0.4, 0.2 um

    (b) repeat for the preceding values of L, but keep W constant at 0.8um. Discuss the results
        obtained, Neglect the effect of channel length and width on the threshold voltage

    Example 1. (5.2.11)

    Ids = (W / L) * (uCox[(Vgs - Vt) * Vds - 0.5 * a * Vds ** 2] / (1 + Vds/(L * Ec))
    for Vds <= V'ds

    V'ds = (Vgs - Vt) / a * 2 / (1 + sqrt(1 + ((Vgs - Vt) / a) * 2 / (L * Ec))
======================================================================================================
