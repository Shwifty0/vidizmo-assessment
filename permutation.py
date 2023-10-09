from itertools import permutations
# Function to return array of permutations
def perm(lst):
    # If input array is empty return the empty list
    if lst == []:
        return lst
    else:
        return list(permutations(lst))


# Permutation using recursion
def permute(lst):

    # Test case 1: if the array is empty
    if len(lst) == 0:
        return []
    # Test case 2: if the array has  only one element
    if len(lst) == 1:
        return [lst]
    
    # empty list
    l = []

    for i in range(len(lst)):
        m = lst[i] # temp var 

        remLst = lst[:i]+ lst[i+1:] # element[:0 and so on] + element [1:] - firt iteration: empty_list + list with remaining elements except for the first element.

        for p in permute(remLst):
            l.append([m] + p)
    return l
arr = [1,2,3]
perm_lst = []
for p in permute(arr):
    perm_lst.append(p)
print(perm_lst)