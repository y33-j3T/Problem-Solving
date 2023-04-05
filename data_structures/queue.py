from collections import deque

q = deque()     # queue

len(q)          # size()
len(q) == 0     # empty()

q[0]            # peek()
q.append('a')   # enqueue('a')
q.popleft()     # dequeue()