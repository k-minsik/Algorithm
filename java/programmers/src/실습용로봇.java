public class 실습용로봇 {
    public static final int[] dy = {1, 0, -1, 0};
    public static final int[] dx = {0, 1, 0, -1};
    public int x, y, i;

    public int[] solution(String command) {
        x = 0;
        y = 0;
        i = 0;

        for(int idx = 0; idx < command.length(); idx++) {
            if (command.charAt(idx) == 'G') {
                y += dy[i];
                x += dx[i];
            } else if (command.charAt(idx) == 'R') {
                i = (i + 1) % 4;
            } else if (command.charAt(idx) == 'L') {
                i = (i + 3) % 4;
            } else {
                y -= dy[i];
                x -= dx[i];
            }
        }

        return new int[] {x, y};
    }
}
