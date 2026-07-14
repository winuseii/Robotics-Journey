# Day-2: Matrix Operations

def mat_shape(A):
    return (len(A), len(A[0]))

def mat_add(A, B):
    return [[a + b for a, b in zip (row_a, row_b)] for row_a, row_b in zip(A, B)]

def mat_scalar_mul(A, scalar):
    return [[a*scalar for a in row] for row in A]

def mat_multiply(A, B):
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)] for row_a in A]

def mat_transpose(A):
    return [list(row) for row in zip(*A)]

def mat_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def mat_vec_multiply(A, v):
    return [sum(a*b for a,b in zip(row,v)) for row in A]

# TEST VCTORS

if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    v = [3, 7]
    
    print("Shape of A:", mat_shape(A))         # (2, 2)
    print("A + B:", mat_add(A, B))             # [[6,8],[10,12]]
    print("2 * A:", mat_scalar_mul(A, 2))      # [[2,4],[6,8]]
    print("A @ B:", mat_multiply(A, B))        # [[19,22],[43,50]]
    print("A^T:", mat_transpose(A))            # [[1,3],[2,4]]
    print("I(3):", mat_identity(3))            # 3x3 identity
    print("Av:", mat_vec_multiply(A, v))       # gave [3, 7]


# i understood more deeply about the uses of zip(). it is very useful for matrix operation and vectors. it allows to seperate the rows as i understand it.
# the command also allows to seperate the columns when we use zip(*A). 

# i learnt about the list() and sum() commands. list() allows us to convert a zip object back into a list (convert back into a matrix). 
# sum() allows us to sum up the elements in a list.

# i understood how to logically create matrix operations in python WITHOUT the use of Numpy (very hard, very fun)

# i also understood the use of line 26 (" if __name__ == "__main__":) which allows us to test the functions we created in the same file without having to import it. 
# it is a very useful command for testing and debugging. it also allows us to run the file as a script without executing the test code. 

