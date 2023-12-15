

def Bisection(function, a, b, output_range, tolerance=1e-6, max_iterations=100):

    if not callable(function):
        raise TypeError("Function not callable")

    midpoint = 0
    for i in range(max_iterations):
        midpoint = (a + b) / 2
        output = function(midpoint)

        if abs(output - output_range) < tolerance:
            return midpoint

        if output < output_range:
            a = midpoint
        else:
            b = midpoint

    return midpoint

    raise Exception("Bisection method did not converge within max iterations")


'''# Desired output range
desired_output_range = 2

# Initial range for x
initial_range = [0, 5]

# Find the value of x that satisfies the nonlinear equation within the desired output range
solution = bisection_method(initial_range[0], initial_range[1], desired_output_range)

# Use the obtained solution for further calculations
# For example, you can feed the solution into another equation
# result = another_equation(solution)

print("Solution for x:", solution)'''
