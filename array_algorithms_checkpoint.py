"""
Checkpoint Algorithms
=====================

Problem 1: Sum of Distinct Elements
Problem 2: Dot Product & Orthogonality Check
"""

# ------------------------------------------------------------
 1 — Sum of Distinct Elements (arrays + nested loops)
# ------------------------------------------------------------
def sum_distinct(set1, set2):
    """
    Returns the sum of all elements that are present in only one of the two sets.
    """
    sum_result = 0

    # Elements in set1 not in set2
    for i in range(len(set1)):
        found = False
        for j in range(len(set2)):
            if set1[i] == set2[j]:
                found = True
        if not found:
            sum_result += set1[i]

    # Elements in set2 not in set1
    for i in range(len(set2)):
        found = False
        for j in range(len(set1)):
            if set2[i] == set1[j]:
                found = True
        if not found:
            sum_result += set2[i]

    return sum_result


# ------------------------------------------------------------
 2 — Dot Product (procedure version)
# ------------------------------------------------------------
def dot_product_procedure(v1, v2, ps_container):
    """
    Procedure version: calculates dot product and stores in ps_container["value"].
    """
    ps = 0
    for i in range(len(v1)):
        ps += v1[i] * v2[i]
    ps_container["value"] = ps


def check_orthogonal_procedure(v1, v2):
    """
    Checks if vectors v1 and v2 are orthogonal using the procedure version.
    """
    ps_container = {"value": 0}
    dot_product_procedure(v1, v2, ps_container)
    return ps_container["value"] == 0


# ------------------------------------------------------------
 2 — Dot Product (function version)
# ------------------------------------------------------------
def dot_product_function(v1, v2):
    """
    Function version: returns the dot product directly.
    """
    ps = 0
    for i in range(len(v1)):
        ps += v1[i] * v2[i]
    return ps


def check_orthogonal_function(v1, v2):
    """
    Checks if vectors v1 and v2 are orthogonal using the function version.
    """
    return dot_product_function(v1, v2) == 0


# ------------------------------------------------------------
# Example Usage
# ------------------------------------------------------------
if __name__ == "__main__":

    # Problem 1
    print("=== Problem 1: Sum of Distinct Elements ===")
    set1 = [3, 1, 7, 9]
    set2 = [2, 4, 1, 9, 3]
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Sum of distinct elements:", sum_distinct(set1, set2))  # Expected: 13

    # Problem 2 - Procedure
    print("\n=== Problem 2: Dot Product (Procedure) ===")
    v1 = [1, 2]
    v2 = [-2, 1]
    print("v1:", v1)
    print("v2:", v2)
    print("Orthogonal?", check_orthogonal_procedure(v1, v2))  # Expected: True

    # Problem 2 - Function
    print("\n=== Problem 2: Dot Product (Function) ===")
    v3 = [3, 4]
    v4 = [4, -3]
    print("v3:", v3)
    print("v4:", v4)
    print("Orthogonal?", check_orthogonal_function(v3, v4))  # Expected: True
