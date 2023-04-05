def bubble_sort(a):
    for i in range(1, len(a)):
        is_sorted = True                # true if a is sorted
        for j in range(len(a) - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_sorted = False       # swap occured, a not sorted yet
        if is_sorted: return            # no swap occured, a already sorted