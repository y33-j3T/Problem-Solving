def quick_sort(a):
    _quick_sort(a, 0, len(a) - 1)

def _quick_sort(a, i, j):
    if i < j:
        pivot_idx = _partition(a, i, j)
        _quick_sort(a, i, pivot_idx - 1)
        _quick_sort(a, pivot_idx + 1, j)

def _partition(a, i, j):
    # partition elements in a[i..j]
    p = a[i]  # pivot, the i-th element
    m = i     # initially S1 and S2 are empty

    for k in range(i + 1, j + 1):   # process unknown region
        if a[k] < p:                # case 2: a[k] to S1 
            m += 1
            a[k], a[m] = a[m], a[k]
            
    a[i], a[m] = a[m], a[i]     # put pivot at right place
    return m                    # pivot's final position