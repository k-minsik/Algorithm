import java.util.*;
public class 귤고르기 {

    class Solution {
        public int solution(int k, int[] ts) {
            int answer = 0;

            Map<Integer, Integer> map = new HashMap<>();

            for (int t : ts) {
                map.put(t, map.getOrDefault(t, 0) + 1);
            }

            List<Integer> list = new ArrayList<>(map.keySet());
            list.sort((a, b) -> map.get(b) - map.get(a));

            for (int t : list) {
                k -= map.get(t);
                answer++;

                if (k <= 0) {
                    return answer;
                }
            }

            return answer;
        }
    }
}
