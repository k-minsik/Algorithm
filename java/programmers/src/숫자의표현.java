public class 숫자의표현 {
    class Solution {
        public int solution(int n) {
            int answer = 0;

            for (int i = 1; i <= n; i++) {
                int num = n;
                int j = i;

                while (num > 0) {
                    num -= j++;

                    if (num == 0) {
                        answer++;
                    }
                }

            }

            return answer;
        }
    }
}
