import java.util.*;
public class 최댓값과최솟값 {

    class Solution {
        private int max, min;
        public String solution(String s) {
            String[] ss = s.split(" ");
            max = Integer.parseInt(ss[0]);
            min = Integer.parseInt(ss[0]);

            for (int i = 0; i < ss.length; i++) {
                int n = Integer.parseInt(ss[i]);

                max = Math.max(max, n);
                min = Math.min(min, n);
            }
            return min + " " + max;
        }
    }
}
