import java.util.*;
public class 연속부분수열합의개수 {

    class Solution {
        public int solution(int[] elements) {
            Set<Integer> set = new HashSet<>();
            int n = elements.length;
            int[] element = new int[n * 2];

            for (int i = 0; i < n; i++) {
                element[i] = elements[i];
                element[i + n] = elements[i];
            }

            for (int i = 0; i < n; i++) {
                for (int j = 1; j < n + 1; j++) {
                    int sum = 0;
                    for (int k = i; k < i + j; k++) {
                        sum += element[k];
                    }
                    set.add(sum);
                }
            }

            return set.size();
        }
    }
}
