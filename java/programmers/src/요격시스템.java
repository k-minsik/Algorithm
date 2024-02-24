import java.util.*;
public class 요격시스템 {

    class Solution {
        public int solution(int[][] targets) {
            int answer = 0;
            Arrays.sort(targets, (a, b) -> a[1] - b[1]);

            double point = -0.1;
            for (int[] t : targets) {
                if (t[0] > point) {
                    point = t[1] - 0.1;
                    answer++;
                }
            }

            return answer;
        }
    }
}
