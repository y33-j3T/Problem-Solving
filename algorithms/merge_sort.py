def merge_sort(a):
    _merge_sort(a, 0, len(a) - 1)

def _merge_sort(a, i, j):
    if i < j:
        mid = (i + j) // 2
        _merge_sort(a, i, mid)
        _merge_sort(a, mid + 1, j)
        _merge(a, i, mid, j)

def _merge(a, i, mid, j):
    # Merges the 2 sorted sub-arrays a[i..mid] and a[mid+1..j]
    # into one sorted sub-array a[i..j]
    tmp = [-1 for _ in len(j - i + 1)]
    l, r, it = i, mid + 1, 0
    # it = next index to store merged item in temp

    while (l <= mid) and (r <= j):
        if a[l] <= a[r]:
            tmp[it] = a[l]
            l += 1
            it += 1
        else:
            tmp[it] = a[r]
            r += 1
            it += 1
    
    # Copy the remaining elements into temp
    while l <= mid:
        tmp[it] = a[l]
        l += 1
        it += 1
    while r <= j:
        tmp[it] = a[r]
        r += 1
        it += 1

    # Copy the result in temp back into the original array a
    for k in range(len(tmp)):
        a[i + k] = tmp[k]
            
    


