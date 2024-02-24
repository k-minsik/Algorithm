import java.util.*;
public class 구명보트 {

    class Solution {
        public int solution(int[] people, int limit) {
            int answer = 0;
            Arrays.sort(people);
            Deque<Integer> dq = new LinkedList<>();

            for (int p : people) {
                dq.offer(p);
            }

            while (!dq.isEmpty()) {
                int min = dq.peekFirst();
                int max = dq.peekLast();

                if (min + max <= limit) {
                    dq.pollFirst();
                    dq.pollLast();
                } else {
                    dq.pollLast();
                }
                answer++;
            }

            return answer;
        }
    }
}
