import java.util.*;
public class 야근지수 {

    class Solution {
        public long solution(int n, int[] works) {
            long answer = 0;
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

            for (int w : works) {
                pq.offer(w);
            }

            while (n > 0 && !pq.isEmpty()) {
                int now = pq.poll();
                int next = pq.isEmpty() ? 0 : pq.peek();
                int work = Math.min(n, now - next);

                if (work == 0) {
                    now -= 1;
                    n -= 1;
                }
                else {
                    now -= work;
                    n -= work;
                }

                if (now != 0) {
                    pq.offer(now);
                }
            }

            while (!pq.isEmpty()) {
                long remain = pq.poll();
                answer += remain * remain;
            }

            return answer;
        }
    }
}
