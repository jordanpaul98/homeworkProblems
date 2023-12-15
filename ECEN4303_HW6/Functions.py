from math import log as ln, exp, sqrt

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
