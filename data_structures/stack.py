from collections import deque

s = deque()     # stack

len(s)          # size()
len(s) == 0     # is_empty()

s[-1]           # peek()
s.append('a')   # push('a')
s.pop()         # pop()