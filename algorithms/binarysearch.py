def binary_search(a, val):
    l = 0
    r = len(a) - 1
    idx = -1
    while (l <= r) and (idx == -1):
        mid = (l + r) // 2
        if a[mid] == val:
            idx = mid
        else:
            if val < a[mid]:
                r = mid - 1
            else:
                l = mid + 1
    return idx