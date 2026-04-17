# Day 1 - Vector operations without NumPy
# Goal: understand what these operations mean geometrically

def add_vectors(v1, v2):
    return [a + b for a, b in zip(v1, v2)]
    pass

def scale_vector(v, scalar):
    return [a*scalar for a in v]   
    pass

def dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))
    pass

# Test it
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print("Sum:", add_vectors(v1, v2))       # expect [5, 7, 9]
print("Scaled:", scale_vector(v1, 2))    # expect [2, 4, 6]
print("Dot:", dot_product(v1, v2))       # expect 32