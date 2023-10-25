
def problem2d5():

    import matplotlib.pyplot as plt
    
    from math import log as ln, sqrt
    
    Vgb_Vfb_2Of = [2, 3, 4, 5]
    y_range = [0.2, 2]
    Ot = 0.0259
    
    def Of2(y, v):

        from bisection import Bisection

        def vgb_vfb(x):
            return x + y * sqrt(x)

        return Bisection(vgb_vfb, 0, 100, v)
    
    def Ot_n(y, v):
        
        return ln(((v ** 2) / (y **2) - Of2(y, v)) / Ot)

    def Ot_n_2Of_ignored(y, v):
        return ln(((v ** 2) / (y ** 2)) / Ot)

    samples = 100
    Y = [y_range[0] + n * (y_range[1] - y_range[0]) / samples for n in range(samples + 1)]
    n = [[Ot_n(y, vgb) for y in Y] for vgb in Vgb_Vfb_2Of]
    n_ignored = [[Ot_n_2Of_ignored(y, vgb) for y in Y] for vgb in Vgb_Vfb_2Of]

    s = [sum(n_vgb) / samples for n_vgb in n]
    s_ignored = [sum(n_vgb) / samples for n_vgb in n_ignored]

    fog, axs = plt.subplots(4, 1, figsize=(12, 20))

    phi = '\u00D8'
    delta = '\u0394'

    for i, axis in enumerate(axs):
        if i == 0:
            axis.set_title(f"{delta}{phi} = {phi}t * n        With [(Vgb - Vfb - 2{phi}f) = {Vgb_Vfb_2Of[i]}]")
        axis.set_ylabel("n")
        axis.plot(Y, n[i], label=f"inner 2{phi}f estimated")
        axis.plot(Y, n_ignored[i], label=F"inner 2{phi}f ignored")
        axis.hlines(s[i], Y[0], Y[-1], label=f"average n={round(s[i], 2)} with Vgb={Vgb_Vfb_2Of[i]}", color='red')
        axis.legend(fontsize='14')

    plt.show()



