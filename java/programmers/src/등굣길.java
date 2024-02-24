public class 등굣길 {
    class Solution {
        public int solution(int c, int r, int[][] puddles) {
            int answer = 0;
            int[][] graph = new int[r][c];
            graph[0][0] = 1;

            for (int[] p : puddles) {
                int y = p[1] - 1;
                int x = p[0] - 1;
                graph[y][x] = -1;
            }

            for (int y = 0; y < r; y++) {
                if (graph[y][0] == -1) break;
                graph[y][0] = 1;
            }

            for (int x = 0; x < c; x++) {
                if (graph[0][x] == -1) break;
                graph[0][x] = 1;
            }

            for (int y = 1; y < r; y++) {
                for (int x = 1; x < c; x++) {
                    if (graph[y][x] == -1) continue;

                    if (graph[y - 1][x] != -1 && graph[y][x - 1] != -1) {
                        graph[y][x] = (graph[y - 1][x] + graph[y][x - 1]) % 1000000007;
                    }
                    else if (graph[y][x - 1] == -1) {
                        graph[y][x] = (graph[y - 1][x]) % 1000000007;
                    }
                    else if (graph[y - 1][x] == -1) {
                        graph[y][x] = (graph[y][x - 1]) % 1000000007;
                    }
                }
            }

            return graph[r-1][c-1];
        }
    }
}
