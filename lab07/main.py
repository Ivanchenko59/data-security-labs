import sys
import math

g, h, q = [int(i) for i in input().split()]

def crack(G, H, Q):
    # Baby-Step Giant-Step algorithm
    m = int(Q ** 0.5) + 1
    baby_steps = {}
    # Precompute the baby steps
    for j in range(m):
        baby_steps[pow(G, j, Q)] = j
    # Giant step: G^(-m)
    gm = pow(G, -m, Q)

    # Search for a match
    for i in range(m):
        target = (H * pow(gm, i, Q)) % Q

        if target in baby_steps:
            return i * m + baby_steps[target]

    # If no match is found
    return None

# Perform the attack
X = crack(g, h, q)

print(X)