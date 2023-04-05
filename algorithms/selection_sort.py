# time: O(n^2)
def selection_sort(a):
    for i in range(len(a) - 1, 0, -1):
        idx = i  # to hold the position of largest element

        # find largest element in unsorted part
        for j in range(i):
            if a[j] > a[idx]:
                idx = j  # j-th is currently the largest

        # swap largest element with last element
        a[idx], a[i] = a[i], a[idx]