# Day 1 - Vector operations without NumPy

def add_vectors(v1, v2):
    return [a + b for a, b in zip(v1, v2)]

def scale_vector(v, scalar):
    return [a*scalar for a in v]   

def dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

# Test vectors:
if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print("Sum:", add_vectors(v1, v2))       
    print("Scaled:", scale_vector(v1, 2))    
    print("Dot:", dot_product(v1, v2))       


# result:
# Sum: [5, 7, 9]
# Scaled: [2, 4, 6]
# Dot: 32

#i learnt about the zip, def, pass and return keywords.
#i also learnt the difference between return and print keywords.
#i learnt how to recall a defined function and how to use it with different arguments.
