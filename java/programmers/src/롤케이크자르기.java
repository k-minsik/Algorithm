import java.util.*;
public class 롤케이크자르기 {

    class Solution {
        public int solution(int[] topping) {
            Map<Integer, Integer> map = new HashMap<>();
            Set<Integer> set = new HashSet<>();
            int answer = 0;

            for (int i = 0; i < topping.length; i++) {
                map.put(topping[i], map.getOrDefault(topping[i], 0) + 1);
            }

            for (int i = 0; i < topping.length; i++) {
                set.add(topping[i]);
                map.put(topping[i], map.getOrDefault(topping[i], 0) - 1);

                if (map.get(topping[i]) == 0) {
                    map.remove(topping[i]);
                }

                if (set.size() == map.size()) {
                    answer++;
                }
            }

            return answer;
        }
    }
}
