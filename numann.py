# In abstract set theory, a construction due to von Neumann represents the natural numbers by sets, as follows:

# 0 = [ ] is the empty set
# 1 = 0 ∪ [ 0 ] = [ 0 ] = [ [ ] ]
# 2 = 1 ∪ [ 1 ] = [ 0, 1 ] = [ [ ], [ [ ] ] ]
# n = n−1 ∪ [ n−1 ] = ...
# Write a function that receives an integer n and produces the representing set.


def rep_set(n):
    return [] if not n else rep_set(n-1) + [rep_set(n-1)]


ans=rep_set(1)
print(ans)