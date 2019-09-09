"""
    Selection and permutation tools
    - **select_m_any** - select m objects from object list (with len = n)
        and returns all combinations. All combinations: n^m
    - **select_Amn** -- select all combination of m different objects from obj_list
        combinations with different order are different
        it is knows as Amn = n! / (n-m)!
    - **select_Cmn** -- select all combination of n different objects from obj_list
        combinations with different order are the same
        it is knows as Cmn = n! / ((n-m)! m!)
"""

def select_n_any(obj_list, m):
    """
        select_n_any selects all combination of n objects from obj_list
        objects can repeat
        cur_idx must be 0 (start of recursion)
    """
    # TODO: make a wrapper for this function to eliminate cur_idx
    # recursion exit
    if m < 1: return []
    if m == 1:
        res = [[o] for o in obj_list]
        return res
    # body
    res = []
    for o in obj_list:
        lists = select_n_any(obj_list, m-1)
        for l in lists:
            l.insert(0, o)
            res.append(l)
    return res

def select_Amn(obj_list, m):
    """
        select_Amn selects all combination of n different objects from obj_list
        combinations with different order are different
    """
    # recursion exit
    if m < 1: return []
    if m == 1:
        res = [[o] for o in obj_list]
        return res
    # body
    res = []
    for o in obj_list:
        lists = select_Amn(obj_list, m-1)
        for l in lists:
            if o not in l:
                l.insert(0, o)
                res.append(l)
    return res

def select_Cmn(obj_list, m, idx = 0):
    """
        select_Cmn selects all combination of n different objects from obj_list
        combinations with different order are the same
    """
    # recursion exit
    if m < 1: return []
    if m == 1:
        res = [[o] for o in obj_list[idx:]]
        return res
    # body
    res = []
    for i,o in enumerate(obj_list[idx:]):
        lists = select_Cmn(obj_list, m-1, i+1)
        for l in lists:
            if o not in l:
                l.insert(0, o)
                res.append(l)
    return res

def test_select_any():
    assert(len(select_n_any([1, 2, 3, 4], 3)) == 4**3)
    assert(len(select_n_any([1, 2, 3, 4], 2)) == 4**2)

def test_select_Amn():
    assert(len(select_Amn([1, 2, 3, 4], 1)) == 4)  # 4! / (4-1)!
    print("A_2,4", select_Amn([1, 2, 3, 4], 2))
    assert(len(select_Amn([1, 2, 3, 4], 2)) == 12) # 4! / (4-2)!
    assert(len(select_Amn([1, 2, 3, 4, 5], 2)) == 20) # 5! / (5-2)!

def test_select_Cmn():
    assert(len(select_Cmn([1, 2, 3, 4], 1)) == 4)  # 4! / (4-1)! 1!
    print("C_2,4", select_Cmn([1, 2, 3, 4], 2))
    assert(len(select_Cmn([1, 2, 3, 4], 2)) == 6) # 4! / (4-2)! 2!
    assert(len(select_Cmn([1, 2, 3, 4, 5], 2)) == 10) # 5! / (5-2)! 2!

if __name__ == "__main__":
    test_select_any()
    test_select_Amn()
    test_select_Cmn()
