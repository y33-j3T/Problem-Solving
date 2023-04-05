from heapq import heapify, heappush, heappop

l1 = [5, 7, 9, 1, 3]                                    # heapq will arrange
l2 = [(2000, "John"), (30, "Billy"), (500, "Andy")]     # accordingly

# heapq only does min heap, so invert everything to do max heap
l1 = [-x for x in l1]
l2 = [(-x, y) for x, y in l2]


h = l2  # example
heapify(h)                   # heap

len(h)                       # size()
len(h) == 0                  # empty()

heappush(h, (-150, "Bob"))   # push((150, "Bob"))
heappop(h)                   # pop()


# custom priority function