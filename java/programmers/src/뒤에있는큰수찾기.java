import java.util.*;
public class 뒤에있는큰수찾기 {
    public int[] solution(int[] numbers) {
        Stack<int[]> st = new Stack<>();
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, -1);

        for (int i = 0; i < numbers.length; i++) {
            while (!st.empty() && st.peek()[0] < numbers[i]) {
                answer[st.pop()[1]] = numbers[i];
            }
            st.push(new int[] {numbers[i], i});
        }

        return answer;
    }
}
