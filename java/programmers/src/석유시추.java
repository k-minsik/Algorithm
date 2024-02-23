import java.util.*;

public class 석유시추 {
    public static final int[] dy = {-1, 0, 1, 0};
    public static final int[] dx = {0, 1, 0, -1};
    public static int r, c, no;
    public static int[][] graph, visited;

    public static int bfs(int y, int x) {
        int count = 1;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{y, x});
        graph[y][x] = no;
        visited[y][x] = 1;

        while (!q.isEmpty()) {
            int[] now = q.poll();
            y = now[0];
            x = now[1];

            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (ny >= 0 && ny < r && nx >= 0 && nx < c && graph[ny][nx] == 1 && visited[ny][nx] == 0) {
                    count++;
                    graph[ny][nx] = no;
                    visited[ny][nx] = 1;
                    q.offer(new int[]{ny, nx});
                }
            }
        }
        return count;
    }

    public int solution(int[][] land) {
        int answer = 0;
        r = land.length;
        c = land[0].length;
        graph = land;
        visited = new int[r][c];
        List<Integer> oil = new ArrayList<>();
        oil.add(0);

        for (int y = 0; y < r; y++) {
            for (int x = 0; x < c; x++) {
                if (graph[y][x] == 1 && visited[y][x] == 0) {
                    no++;
                    oil.add(bfs(y, x));
                }
            }
        }

        for (int x = 0; x < c; x++) {
            Set<Integer> unique = new HashSet<>();
            int tempAnswer = 0;
            for (int y = 0; y < r; y++) {
                unique.add(graph[y][x]);
            }
            for (int num : unique) {
                tempAnswer += oil.get(num);
            }
            answer = Math.max(answer, tempAnswer);
        }

        return answer;
    }
}
