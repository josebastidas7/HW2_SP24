import math

def Probability(PDF, args, c, GT=True):
    """
    Calculate the probability using Simpson's 1/3 rule.

    Parameters:
    - PDF: Gaussian/normal probability density function callback
    - args: Tuple containing μ and σ
    - c: Upper limit of integration
    - GT: Boolean indicating if we want the probability of x being greater than c (GT=True) or less than c (GT=False)

    Returns:
    - Probability value
    """
    # Define the limits of integration
    lower_limit = args[0] - 5 * args[1]
    upper_limit = c

    # Initialize variables for Simpson's 1/3 rule
    h = (upper_limit - lower_limit) / 1000
    result = PDF((lower_limit, *args))
    
    # Simpson's 1/3 rule
    for i in range(1, 1000):
        x = lower_limit + i * h
        coefficient = 4 if i % 2 == 1 else 2
        result += coefficient * PDF((x, *args))
    
    result += PDF((upper_limit, *args))

    result *= h / 3

    return result if GT else 1 - result

def normal_pdf(data):
    """
    Gaussian/normal probability density function callback.

    Parameters:
    - data: Tuple containing x, μ, σ

    Returns:
    - PDF value
    """
    x, mean, std_dev = data
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-(x - mean)**2 / (2 * std_dev**2))

def main():
    # Test cases
    result1 = Probability(normal_pdf, (100, 12.5), 105, GT=False)
    result2 = Probability(normal_pdf, (100, 3), 100 + 2 * 3, GT=True)

    # Print results
    print(f"P(x<105|N(100,12.5)) = {result1:.2f}")
    print(f"P(x>{100 + 2 * 3}|N(100, 3)) = {result2:.2f}")

if __name__ == "__main__":
    main()
