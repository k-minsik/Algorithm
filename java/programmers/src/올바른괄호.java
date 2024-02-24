import java.util.*;
public class 올바른괄호 {

    class Solution {
        boolean solution(String s) {
            int count = 0;

            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);

                if (c == '(') {
                    count++;
                } else {
                    if (count == 0) {
                        return false;
                    } else {
                        count--;
                    }
                }
            }
            return count == 0;
        }
    }
}
