import java.util.ArrayList;

public class DFS {

    /**
    * @param source Vertex to begin with.
    * @param parent Parents of vertices. Initialized with -1.
    * @param visited Checklist of visited vertices. Initialized with 0.
    * @param adjList Adjacency List. Initialized with neighbor vertices and their respective weighs
    */
    public static void _DFS(int source, int[] parent, int[] visited, ArrayList<ArrayList<IntegerPair>> adjList) {
        visited[source] = 1;

        for (IntegerPair v : adjList.get(source)) {
            int val = v.first();
            if (visited[val] == 0) {
                parent[val] = source;
                _DFS(val, parent, visited, adjList);
            }
        }

        // after DFS stops, we can use info stored in visited / parent
    }
}
