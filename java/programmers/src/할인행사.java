import java.util.*;
public class 할인행사 {

    class Solution {
        public boolean compareMap(Map<String, Integer> a, Map<String, Integer> b) {
            if (a.size() != b.size()) return false;

            for (String key : a.keySet()) {
                if (!b.containsKey(key)) return false;
                if (a.get(key) != b.get(key)) return false;
            }

            return true;
        }

        public int solution(String[] want, int[] number, String[] discount) {
            int answer = 0;
            Map<String, Integer> map = new HashMap<>();

            for (int i = 0; i < want.length; i++) {
                map.put(want[i], number[i]);
            }

            for (int i = 0; i < discount.length - 9; i++) {
                Map<String, Integer> temp = new HashMap<>();

                for (int j = 0; j < 10; j++) {
                    temp.put(discount[i + j], temp.getOrDefault(discount[i + j], 0) + 1);
                }

                if (compareMap(map, temp)) answer++;
            }

            return answer;
        }
    }
}
