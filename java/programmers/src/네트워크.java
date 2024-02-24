import java.util.*;
public class 네트워크 {

    class Solution {
        public static int[] visited;
        public static ArrayList<ArrayList<Integer>> adj;

        public void dfs(int now) {
            for (int i : adj.get(now)) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    dfs(i);
                }
            }
        }

        public int solution(int n, int[][] computers) {
            int answer = 0;
            adj = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                ArrayList<Integer> temp = new ArrayList<>();
                for (int j = 0; j < n; j++) {
                    if (computers[i][j] == 1) {
                        if (i != j) {
                            temp.add(j);
                        }
                    }
                }
                adj.add(temp);
            }

            visited = new int[n];
            for (int i = 0; i < n; i++) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    dfs(i);
                    answer++;
                }
            }
            return answer;
        }
    }
}
