def Bisection(function, a, b, output_range, tolerance=1e-6, max_iterations=100):

    if not callable(function):
        raise TypeError("Function isnt callable")

    for i in range(max_iterations):
        midpoint = (a + b) / 2
        output = function(midpoint)

        if abs(output - output_range) < tolerance:
            return midpoint

        if output < output_range:
            a = midpoint
        else:
            b = midpoint

    raise Exception("Did not coverge")
  
