import java.util.*;
public class 영어끝말잇기 {

    class Solution {
        public int[] solution(int n, String[] words) {
            Map<String, Boolean> check = new HashMap<>();
            check.put(words[0], true);
            char before = words[0].charAt(words[0].length() - 1);

            for (int i = 1; i < words.length; i++) {
                char after = words[i].charAt(0);
                if (before != after) {
                    return new int[] {i % n + 1, i / n + 1};
                }

                if (check.containsKey(words[i])) {
                    return new int[] {i % n + 1, i / n + 1};
                } else {
                    check.put(words[i], true);
                }
                before = words[i].charAt(words[i].length() - 1);;
            }


            return new int[] {0, 0};
        }
    }
}
