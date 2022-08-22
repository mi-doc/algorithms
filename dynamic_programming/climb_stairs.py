def climbStairsIterative(n):
    """
    The FASTEST solution
    """
    if n in (0,1):
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b

def climbStairsRecursive(n):
    """
    This approach is far from the best due to time and space consumption
    """
    if n in (0,1,2):
        return n
    return climbStairsRecursive(n-1)+climbStairsRecursive(n-2)

def climbStairsDict(n):
    """
    VERY SLOW!
    The dictionary is used to store results for numbers that have already been
    processed -> don't need to calculate them again
    """
    dic = { 0:0, 1:1, 2:2 }
    if n not in dic:
        dic[n] = climbStairsDict(n-1) + climbStairsDict(n-2)
    return dic[n]

if __name__ == '__main__':
    from speed_tests import speed_contest
    val = 20

    speed_contest([
        "climbStairsIterative(val)",
        'climbStairsRecursive(val)',
        'climbStairsDict(val)'], globals=globals()
    )