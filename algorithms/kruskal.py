from data_structures.ufds import UnionFind

# 1. Make edge list, sort it by weight
# 2. Set up UFDS, initialize with no. of vertices
# 3. For edge in edge list:
#       if (u, v) are not in the same set:
#           update whatever
#           union set containing u & v

def kruskal():
    # Graph in Figure 4.10 left, format: list of weighted edges
    # This example shows another form of reading graph input
    # 5 7
    # 0 1 4
    # 0 2 4
    # 0 3 6
    # 0 4 6
    # 1 2 2
    # 2 3 8
    # 3 4 9

    f = open("mst_in.txt", "r")

    V, E = map(int, f.readline().split(" "))        # no. of vertex, edge

    # Kruskal's algorithm
    EL = []                                         # edge list
    for _ in range(E):
        u, v, w = map(int, f.readline().split(" ")) # read as (u, v, w)
        EL.append((w, u, v))                        # reorder as (w, u, v)
    EL.sort()                                       # sort by w, O(E log E)

    num_taken = 0                                   # no. of edge taken for MST
    mst_cost = 0                                    # total edge weight for MST
    UF = UnionFind(V)                               # all V are disjoint sets

    for i in range(E):                              # for each edge, O(E)
        if num_taken == V - 1:
            break
        w, u, v = EL[i]
        if (not UF.is_same_set(u, v)):              # check
            num_taken += 1                          # 1 more edge is taken
            mst_cost += w                           # add w of this edge
            UF.union_set(u, v)                      # link them
    
    # note: the runtime cost of UFDS is very light
    # note: the number of disjoint sets must eventually be 1 for a valid MST