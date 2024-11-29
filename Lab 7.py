import math

def discrete_log_bsgs(G, H, Q):
    """
    Solve the discrete logarithm problem using Baby-step Giant-step algorithm.
    Find X such that G^X mod Q = H.
    """
    m = int(math.ceil(math.sqrt(Q)))  
    value_table = {}

    
    for j in range(m):
        value = pow(G, j, Q)
        value_table[value] = j

    
    inv = pow(G, -m, Q)

    
    current = H
    for i in range(m):
        if current in value_table:
            return i * m + value_table[current]
        current = (current * inv) % Q

    return None  



if __name__ == "__main__":
    
    G, H, Q = map(int, input().strip().split())

    
    X = discrete_log_bsgs(G, H, Q)

    
    if X is not None:
        print(X)
    else:
        print("No solution found.")
