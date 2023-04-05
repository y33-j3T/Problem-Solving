class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.set_size = [1 for i in range(N)]
        self.num_sets = N

    def find_set(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.find_set(self.parent[i])
            return self.parent[i]
    
    def is_same_set(self, i, j):
        return self.find_set[i] == self.find_set[j]
    
    def union_set(self, i, j):
        if self.is_same_set(i, j): return

        self.num_sets -= 1
        x = self.find_set(i)
        y = self.find_set(j)

        # use rank to keep tree short
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.set_size[x] += self.set_size[y]
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.set_size[y] += self.set_size[x]

    def num_disjoint_sets(self):
        return self.num_sets
    
    def size_of_set(self, i):
        return self.set_size[self.find_set(i)]
