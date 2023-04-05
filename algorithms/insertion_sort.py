# time: O(n^2), best O(n)
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]  # current element considered for insertion

        j = i - 1   # compare to 1st element in front
        while j >= 0 and a[j] > key:  # element in front larger
            a[j + 1] = a[j]           # so point to element in front
            j -= 1  # compare to 2nd, 3rd, ... element in front

        a[j + 1] = key  # loop till it finds the right place
