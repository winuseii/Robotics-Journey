# Day-3: Advanced Matrix Operations
# (Gaussian elimination, matrix inverse, determinant)

from day2_matrix_ops import mat_multiply, mat_identity, mat_shape

def determinant(A):
    n = mat_shape(A)
    if n == (1, 1):
        return A[0][0]
    if n == (2, 2):
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0
    if n == (3, 3):
        minor00 = A[1][1] * A[2][2] - A[1][2] * A[2][1]
        minor01 = A[1][0] * A[2][2] - A[1][2] * A[2][0]
        minor02 = A[1][0] * A[2][1] - A[1][1] * A[2][0]
        det = A[0][0]*minor00 - A[0][1]*minor01 + A[0][2]*minor02
    return det

def mat_inverse(A):
    n = len(A)
    
    if abs(determinant(A)) < 1e-10:
        raise ValueError("Matrix is singular - no inverse exists")
    
    # Build augmented matrix [A | I]
    identity = mat_identity(n)
    aug = [A[i][:] + identity[i][:] for i in range(n)]
    
    # Forward elimination - make upper triangular
    for i in range(n):
        # Make pivot = 1 by dividing entire row by pivot value
        pivot = aug[i][i]
        aug[i] = [x / pivot for x in aug[i]]
        
        # Eliminate column i in ALL other rows (not just below)
        for j in range(n):
            if i == j:
                continue
            factor = aug[j][i]
            aug[j] = [aug[j][k] - factor * aug[i][k] 
                      for k in range(2*n)]
    
    # Extract right half — that's the inverse
    inverse = [aug[i][n:] for i in range(n)]
    return inverse

# Tests
if __name__ == "__main__":
    A = [[2, 1], [5, 3]]
    A_inv = mat_inverse(A)
    print("A_inv:", A_inv)
    check = mat_multiply(A, A_inv)
    print("A @ A_inv:")
    for row in check:
        print([round(x, 6) for x in row])  # should be identity
    
    # Singular matrix should raise error
    try:
        mat_inverse([[1,2],[2,4]])
    except ValueError as e:
        print("Caught expected error:", e)
    
    
# ---- TESTS ----
if __name__ == "__main__":
    import math
   # Test 2x2 
    A = [[2, 1], 
         [5, 3]]
    
    det = determinant(A)
    print(f"det(A) = {det}")            # 1
    
    A_inv = mat_inverse(A)
    print("A_inv:", A_inv)              # [[3,-1],[-5,2]]
    
    product = mat_multiply(A, A_inv)
    print("A @ A_inv:", product)        # [[1,0],[0,1]] (identity)
    
    # Test 3x3
    B = [[2, 2, 3],
         [4, 9, 6],
         [9, 8, 1]]
    B_det = determinant(B)                # 0
    print(f"det(B) = {B_det}")
    B_inv = mat_inverse(B)                # 
    print("B_inv:", B_inv)
    check = mat_multiply(B, B_inv)        
    print(f"B @ B_inv: {check}") 


    # abs() is a function used to get the absolute value of a number. 
    # It is useful in this context to check if the matrix is singular.

    # learnt about determinant and inverses and how to calculate it for 2x2 and 3x3 matrices.
