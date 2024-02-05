def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Use the Secant Method to find the root of fcn(x) in the neighborhood of x0 and x1.

    Parameters:
    - fcn: The function for which we want to find the root
    - x0, x1: Two x values in the neighborhood of the root
    - maxiter: Exit if the number of iterations equals this number
    - xtol: Exit if |xnewest - xprevious| < xtol

    Returns:
    - The final estimate of the root (most recent new x value)
    """
    # Initialize variables
    x_prev, x_curr = x0, x1

    for _ in range(maxiter):
        # Calculate the new x value using the Secant method
        x_new = x_curr - fcn(x_curr) * (x_curr - x_prev) / (fcn(x_curr) - fcn(x_prev))

        # Check convergence
        if abs(x_new - x_curr) < xtol:
            return x_new

        # Update values for the next iteration
        x_prev, x_curr = x_curr, x_new

    return x_curr

def main():
    # Test cases
    result1 = Secant(lambda x: x**3 - math.cos(x), 1, 2, maxiter=5, xtol=1e-4)
    result2 = Secant(lambda x: 3 * math.cos(2 * x), 1, 2, maxiter=15, xtol=1e-8)
    result3 = Secant(lambda x: 3 * math.cos(2 * x), 1, 2, maxiter=3, xtol=1e-8)

    # Print results
    print(f"Root of x^3 - cos(x) with maxiter=5, xtol=1e-4: {result1:.5f}")
    print(f"Root of 3 * cos(2x) with maxiter=15, xtol=1e-8: {result2:.5f}")
    print(f"Root of 3 * cos(2x) with maxiter=3, xtol=1e-8: {result3:.5f}")

if __name__ == "__main__":
    main()
