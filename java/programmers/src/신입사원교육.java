import java.util.*;

public class 신입사원교육 {
    public int solution(int[] ability, int number) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int a : ability) {
            pq.offer(a);
        }

        for (int i = 0; i < number; i++) {
            int first = pq.poll();
            int second = pq.poll();
            int hap = first + second;
            pq.offer(hap);
            pq.offer(hap);
        }

        while (!pq.isEmpty()) {
            answer += pq.poll();
        }

        return answer;
    }
}
