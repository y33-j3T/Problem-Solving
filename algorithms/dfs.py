# To modify DFS to suit your use case, recognize the core parameters to be
# `def dfs(source, structure, visited, ...)`.
# It traverses some data structure `structure`, 
# starting from some starting point `source`,
# and records which point is visited in `visited`.

# To get more information, simply add parameters to DFS.
# Either pass in a referenced object or pass in a value and return a new value.
# Eg. Add c=[0] to count no. of coordinates searched with c[0] += dfs(...) 
#   and return c[0].


def dfs(adj_list, source_node, visited, parents):
    """
    Depth-first search for trees.
    When the algorithm ends, we use the information stored in `visited` or `parents`.

    Parameters:
        source_node (T): Vertex to begin with.
        parents (list of T): Parents of vertices, initialized with -1.
        visited (list of T): Visited vertices, initialized with 0.
        adj_list (dict of T: list of tuple of (T, int)): 
            Adjacency list, initialized with neighbor vertices and 
            their respective edge weights.

    Returns:
        None.
    """
    visited[source_node] = True

    for (neighbor_node, weight) in adj_list.get(source_node):
        if not visited[neighbor_node]:
            # record whatever
            parents[neighbor_node] = source_node

            # continue algorithm
            dfs(adj_list, neighbor_node, visited, parents)


# given some matrix
matrix = [[1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
N, M = len(matrix), len(matrix[0])
# do not do this: visited = [[False] * M] * N
visited = [[False for _ in range(M)] for _ in range(N)]
# top, right, bottom, left, top-left, top-right, bottom-right, bottom-left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
def dfs(matrix, source_coor, visited, directions=DIRECTIONS):
    """
    Depth-first search for matrices.
    When the algorithm ends, we use the information stored in `visited`.
    
    Parameters:
        source_coor (T): Coordinate to begin with.
        matrix (list of T): Matrix to DFS on, initialized with 1s and 0s.
        visited (list of T): Visited coordinates, initialized with Falses.
        directions (list of tuple of (int, int)): 
            Directions to consider when DFS-ing.

    Returns:
        None.
    """
    i, j = source_coor[0], source_coor[1]  # x, y source coordinate
    visited[i][j] = True

    for d in directions:
        # next coordinates
        next_i = i + d[0]
        next_j = j + d[1]
        
        # validity checks, order matters
        is_valid_bounds = (0 <= next_i < N) and (0 <= next_j < M)
        if not is_valid_bounds: continue

        is_valid_obj = (matrix[next_i][next_j] == 1)
        if not is_valid_obj: continue

        is_visited = visited[next_i][next_j]
        if is_visited: continue
        
        # continue algorithm
        dfs(matrix, (next_i, next_j), visited)
