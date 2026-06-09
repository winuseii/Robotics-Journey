# Day-3: Advanced Matrix Operations
# Gaussian elimination, matrix inverse, determinant

from day2_matrix_ops import mat_multiply, mat_identity, mat_shape

def forward_elimination(A, swap=False):
    U = [row[:] for row in A]
    sign = 1
    for i in range(len(A)):
        if U[i][i] == 0:
            for k in range(i+1, len(A)):
                if U[k][i] != 0:
                    U[i], U[k] = U[k], U[i]
                    sign *= -1
                    break
        
        for j in range(i+1, len(A)):
            if U[i][i] == 0:
                continue
            factor = U[j][i] / U[i][i]
            for k in range(i, len(A)):
                U[j][k] -= factor * U[i][k]    
    if swap:
        return U, sign
    return U

def determinant(A):
    U, sign = forward_elimination(A, swap=True)

    det = sign
    for i in range(len(U)):
        det *= U[i][i]

    return det

def mat_inverse(A):
    n = len(A)

    identity = mat_identity(n)
    aug = [A[i][:] + identity[i][:] for i in range(n)]

    aug = forward_elimination(aug, swap=False)

    for i in range(n-1, -1, -1):
        if aug[i][i] == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        for j in range(i-1, -1, -1):
            factor = aug[j][i] / aug[i][i]
            for k in range(2*n):
                aug[j][k] -= factor * aug[i][k]

    for i in range(n):
        pivot = aug[i][i]
        for k in range(2*n):
            aug[i][k] /= pivot

    # Extract inverse (right half)
    inv = [row[n:] for row in aug]
    return inv
# ---- TESTS ----
if __name__ == "__main__":
    import math
    
    A = [[2, 1], 
         [5, 3]]
    
    det = determinant(A)
    print(f"det(A) = {det}")            # 1
    
    A_inv = mat_inverse(A)
    print("A_inv:", A_inv)              # [[3,-1],[-5,2]]
    
    product = mat_multiply(A, A_inv)
    print("A @ A_inv:", product)        # [[1,0],[0,1]]
    
    # Test 3x3
    B = [[1, 2, 3],
         [0, 1, 4],
         [5, 6, 3]]
    B_det = determinant(B)
    print(f"det(B) = {B_det}")
    B_inv = mat_inverse(B)
    check = mat_multiply(B, B_inv)
    print("B @ B_inv:")
    for row in check:
        print([round(x, 6) for x in row])  