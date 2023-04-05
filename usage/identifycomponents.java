import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedOutputStream;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class identifycomponents {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedOutputStream out = new BufferedOutputStream(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        // int[][] adjMat = new int[n][n];
        ArrayList<ArrayList<IntegerPair>> adjList = new ArrayList<ArrayList<IntegerPair>>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            ArrayList<IntegerPair> newList = new ArrayList<>();

            for (int j = 0; j < n; j++) {
                int temp = Integer.parseInt(st.nextToken());
                // adjMat[i][j] = temp;
                if (temp != 0) newList.add(new IntegerPair(j, temp));
            }

            adjList.add(newList);
        }

        int componentCount = 0;
        DFS dfs = new DFS();

        int[] visited = new int[n];
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            visited[i] = 0;
            parent[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                componentCount++;
                dfs._DFS(i, parent, visited, adjList); // or _BFS
            }
        }
    }
}
