
import java.util.*;
public class JadenCase문자열만들기 {

    class Solution {
        public String solution(String s) {
            String answer = " ";
            String[] ss = s.split("");

            for (int i = 0; i < ss.length; i++) {
                if (answer.charAt(answer.length() - 1) == ' ') {
                    answer += ss[i].toUpperCase();
                } else {
                    answer += ss[i].toLowerCase();
                }
            }

            return answer.substring(1);
        }
    }
}
