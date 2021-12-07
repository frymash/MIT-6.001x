#!/usr/local/bin python3

from icecream import ic

def merge(left,right) -> list:

    """
    inputs:
    - left: a sorted sublist; 
            left side of an unsorted list broken into 2 by merge_sort()

    - right: a sorted sublist;
            right side of an unsorted list broken into 2 by merge_sort()

    returns a sorted list (result) with the elements of left and right combined
    """

    result = []
    i,j = 0,0

    # Compare the 1st elt of left with the 1st elt of right.

    while i != len(left) and j != len(right):
        
        # If the 1st elt of left is smaller, add it to result and increment i
        # such that the 2nd elt of left can be evaluated.
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            ic(i,result)

        # Else, the 1st elt of right is smaller. Hence, it must be added to
        # result such that the 2nd elt of right can be evaluated.
        else:
            result.append(right[j])
            j += 1
            ic(j,result)

    # The list with smaller elements will often be exhausted first in the
    # comparison. If that happens, simply add the remaining elements from 
    # the other non-empty list into result

    while i != len(left):
        result.append(left[i])
        i += 1
        ic(i,result)
        
    while j != len(right):
        result.append(right[j])
        j += 1
        ic(j,result)

    # Left and right are now merged and sorted. Return result.
    ic(result)
    return result
    


def merge_sort(L) -> list:

    """
    inputs:
    - L: an unsorted list

    returns a sorted version of L -> list
    """

    # Base case: if list has length 0 or 1, the list is already sorted
    if len(L) < 2:
        return L[:]
    
    # Recursive case: for any list with len >= 2, break them up into
    # half before sorting and merging them
    else:
        mid = len(L) // 2
        left = ic(merge_sort(L[:mid]))
        right = ic(merge_sort(L[mid:]))
        return merge(left,right)

# Test trial 1 (should return [1,2,3,4,5,6,7,8])
ic(merge_sort([6,3,2,4,5,1,8,7]))

# Test trial 2 (should return [1,2,3,4,5,6,7,8])
ic(merge_sort([8,1,5,6,3,7,4,2]))
