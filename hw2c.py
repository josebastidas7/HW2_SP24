import numpy as np

def GaussSeidel(Aaug, x, Niter=15):
    """
    Use the Gauss-Seidel method to estimate the solution to a set of N linear equations.

    Parameters:
    - Aaug: Augmented matrix [A | b]
    - x: Initial guess vector
    - Niter: Number of iterations to compute

    Returns:
    - The final new x vector
    """
    # Ensure the matrix is diagonal dominant
    A = Aaug[:, :-1]
    b = Aaug[:, -1]
    assert np.all(np.abs(np.diag(A)) >= np.sum(np.abs(A), axis=1) - np.abs(np.diag(A))), "Matrix not diagonal dominant"

    # Perform Gauss-Seidel iterations
    for _ in range(Niter):
        for i in range(len(x)):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

def main():
    # Test cases
    Aaug1 = np.array([[4, -1, 0, 3], [2, 5, -1, 9], [1, 1, 4, 7]], dtype=float)
    x1 = np.zeros_like(Aaug1[0, :-1])
    result1 = GaussSeidel(Aaug1, x1)

    Aaug2 = np.array([[4, -1, 0, 3], [2, 5, -1, 9], [1, 1, 4, 7]], dtype=float)
    x2 = np.zeros_like(Aaug2[0, :-1])
    result2 = GaussSeidel(Aaug2, x2, Niter=10)

    # Print results
    print("Solution for set of linear equations 1:")
    print(result1)
    print("\nSolution for set of linear equations 2:")
    print(result2)

if __name__ == "__main__":
    main()
  
