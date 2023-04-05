import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

public class toposort {

    /**
    * Topological Sort: Khan's algorithm (modified BFS), on DAG only
    * @param parent Parents of vertices. Initialized with -1.
    * @param indeg In-degree of vertices. Initialized with 0.
    */
    public static void _toposortBFS(int numVertices, int[] parent, int[] indeg, ArrayList<IntegerTriplet> edgeList, ArrayList<ArrayList<IntegerPair>> adjList) {
        // initialization
        for (IntegerTriplet edge : edgeList) {
            int v = edge.second();
            indeg[v]++;
        }

        Queue<Integer> q = new LinkedList<>();
        for (int v : indeg) {
            if (indeg[v] == 0) q.add(v);
        }

        // main loop
        ArrayList<Integer> sortedList = new ArrayList<>();
        while (!q.isEmpty()) {
            int u = q.poll();
            sortedList.add(u);

            for (IntegerPair v : adjList.get(u)) {
                if (indeg[v] > 0) indeg[v]--;

                if (indeg[v] == 0) {
                    parent[v] = u;
                    q.enqueue(v);
                }
            }
        }

        // output
        for (Integer i : sortedList) {
            System.out.printf("%d ", i);
        }
    }

    /**
    * Topological Sort: DFS, on DAG only
    * @param parent Parents of vertices. Initialized with -1.
    * @param indeg In-degree of vertices. Initialized with 0.
    */
    public static void _toposortDFS(int numVertices, int[] parent, int[] visited, ArrayList<ArrayList<IntegerPair>> adjList) {
        ArrayList<Integer> sortedList = new ArrayList<>();

        for (int i = 0; i < numVertices; i++) {
            if (visited[i] == 0) _DFS(i, parent, visited, adjList, sortedList);
        }

        // reverse toposort and output it
        for (int i = sortedList.size() - 1; i >= 0; i--) {
            System.out.printf("%d ", sortedList.get(i));
        }
    }

    public static void _DFS(int source, int[] parent, int[] visited, ArrayList<ArrayList<IntegerPair>> adjList, ArrayList<Integer> sortedList) {
        visited[source] = 1;
        for (IntegerPair v : adjList.get(source)) {
            int temp = v.first();
            if (visited[temp] == 0) {
                parent[temp] = source;
                _DFS(temp);
            }
        }
        sortedList.add(source);
    }
}
