import java.util.*;

public class 체육대회 {
    class Solution {
        public static int n, m, answer;
        public static int[] visited = new int[11];
        public static int[][] abilitys;

        public int dfs(int score, int depth) {
            if (depth == m) {
                return score;
            }

            for (int i = 0; i < n; i++) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    answer = Math.max(answer, dfs(score + abilitys[i][depth], depth + 1));
                    visited[i] = 0;
                }
            }
            return answer;

        }

        public int solution(int[][] ability) {
            abilitys = ability;
            n = ability.length;
            m = ability[0].length;

            return dfs(0, 0);
        }
    }
}
