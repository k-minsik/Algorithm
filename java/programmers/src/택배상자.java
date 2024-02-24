import java.util.*;
public class 택배상자 {

    class Solution {
        public int solution(int[] order) {
            int answer = 0;
            int n = order.length;
            Stack<Integer> st = new Stack<>();
            Queue<Integer> q = new LinkedList<>();

            for (int i = 0; i < n; i++) {
                q.offer(i + 1);
            }

            int i = 0;
            while (i < n) {
                int now = order[i];
                if (!q.isEmpty() && now == q.peek()) {
                    q.poll();
                    answer += 1;
                    i++;
                } else if (!st.empty() && now == st.peek()) {
                    st.pop();
                    answer += 1;
                    i++;
                } else if (!q.isEmpty()) {
                    st.push(q.poll());
                } else if (q.isEmpty() && now != st.peek()) {
                    break;
                }

            }
            return answer;
        }
    }
}
