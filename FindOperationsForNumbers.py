"""
    Puzzle for kids: given some numbers, without any operations and result.
    Insert (write) mathematical signs (binary operators) or leave empty space.
    Empty space means concatenation: e.g. 1 2 means 12.
    Result of all operation must be the same as the given result

    Example 1
    1 2 3 4 5 = 41 set operators
    12 + 34 - 5 = 41 # one variant of solution

    TODO: add parenthesises
"""

op_str = ['+', '-', '*', '/', '']

def select_n_any(obj_list, n, cur_idx):
    """
        select_n_any selects all combination of n objects from obj_list
        objects can repeat
        cur_idx must be 0 (start of recursion)
    """
    # TODO: make a wrapper for this function to eliminate cur_idx
    # recursion exit
    if cur_idx+1 == n:
        res = [[o] for o in obj_list]
        return res
    # body
    res = []
    for o in obj_list:
        lists = select_n_any(obj_list, n, cur_idx+1)
        for l in lists:
            l.insert(0, o)
            res.append(l)
    return res

def test_select_any():
    s = select_n_any([1, 2, 3], 2, 0)
    #s = select_n_any(['+', '-', '*', '/', "><"], 4, 0)
    #print(s)
    assert([[1, 1], [1, 2], [1, 3],
            [2, 1], [2, 2], [2, 3],
            [3, 1], [3, 2], [3, 3],] == s)
    

def check_op_set(op_set, nums, result):
    """
        checks if numbers and operation gives the correct result
            and returns expresstion as a string
    """
    assert(len(op_set)+1 == len(nums))
    res = [str(nums[0])]
    for op, num in zip(op_set, nums[1:]):
        res.append(op)
        res.append(str(num))
    res_str = "".join(res)
    if eval(res_str) == result:
        return res_str
    else:
        return None

def solve_equation(nums, res):
    """
        The solution to the puzzle in the start of the unit
    """
    op_list = select_n_any(op_str, len(nums)-1, 0)
    for op_set in op_list:
        res_str = check_op_set(op_set, nums, res)
        if res_str:
            print(res_str, '=', res)

if __name__ == "__main__":
    test_select_any()
    solve_equation([1, 2, 3, 4, 5], 41)
    solve_equation([2, 4, 6], 2)
    solve_equation([2, 4, 6], 4)
    solve_equation([2, 4, 6], 14)
    solve_equation([2, 4, 6], 20)
    solve_equation([2, 4, 6], 48)
    solve_equation([2, 4, 6], 92)
