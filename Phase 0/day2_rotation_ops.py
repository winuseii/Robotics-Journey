# Day-2: Rotation Matrices

import math
from day2_matrix_ops import mat_multiply, mat_vec_multiply, mat_transpose

def rotation_matrix_2d(theta_degrees):
    theta = math.radians(theta_degrees)
    return [
        [math.cos(theta), -math.sin(theta)],
        [math.sin(theta), math.cos(theta)]
    ]

def rotate_point(point, theta_degrees):
    R = rotation_matrix_2d(theta_degrees)
    return mat_vec_multiply(R, point)

def chain_rotations(theta1, theta2):
    R1 = rotation_matrix_2d(theta1)
    R2 = rotation_matrix_2d(theta2)
    return mat_multiply(R1, R2)

# ---- TESTS ----
if __name__ == "__main__":
    # Rotating [1, 0] by 90 degrees should give [0, 1]
    print("90° rotation of [1,0]:", rotate_point([1, 0], 90))
    
    # Rotating [1, 0] by 45 then 45 = same as rotating by 90
    R_combined = chain_rotations(45, 45)
    print("45+45 combined:", mat_vec_multiply(R_combined, [1, 0]))
    
    # R^T should be R^(-1): rotating 90 then -90 = identity action
    R = rotation_matrix_2d(90)
    R_inv = mat_transpose(R)
    should_be_identity = mat_multiply(R, R_inv)
    print("R @ R^T (should be identity):", should_be_identity)


# i understood how to imprt functions from another python file and use it in the currennt file (cool asf)
# i learn about rotation matrices and how imprtant it will be for me as an aspiring robotics engineer
# R^T = R^-1 for rotation matrices.
