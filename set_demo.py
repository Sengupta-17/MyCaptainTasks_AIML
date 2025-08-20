# Defining two sample sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print("-" * 25)

# 1. Union of sets
union_operator = set_a | set_b
union_method = set_a.union(set_b)

print("1. Union (| or .union())")
print(f"   Using Operator ('|'): {union_operator}")
print(f"   Using Method (.union()): {union_method}")
print("-" * 25)


# 2. Intersection of sets
intersection_operator = set_a & set_b
intersection_method = set_a.intersection(set_b)

print("2. Intersection (& or .intersection())")
print(f"   Using Operator ('&'): {intersection_operator}")
print(f"   Using Method (.intersection()): {intersection_method}")
print("-" * 25)


# 3. Difference of sets
diff_a_b = set_a - set_b
diff_b_a = set_b.difference(set_a)

print("3. Difference (- or .difference())")
print(f"   Elements in A but not in B (A - B): {diff_a_b}")
print(f"   Elements in B but not in A (B - A): {diff_b_a}")
print("-" * 25)


# 4. Symmetric Difference of sets
sym_diff_operator = set_a ^ set_b
sym_diff_method = set_a.symmetric_difference(set_b)

print("4. Symmetric Difference (^ or .symmetric_difference())")
print(f"   Using Operator ('^'): {sym_diff_operator}")
print(f"   Using Method (.symmetric_difference()): {sym_diff_method}")
print("-" * 25)
