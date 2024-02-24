import java.util.*;
public class 이진변환반복하기 {

    class Solution {
        public int[] solution(String s) {
            int[] answer = new int[2];

            while (!s.equals("1")) {
                int before = s.length();
                s = s.replaceAll("0", "");
                int after = s.length();
                s = Integer.toBinaryString(after);
                answer[0] += 1;
                answer[1] += before - after;

            }

            return answer;
        }
    }
}
