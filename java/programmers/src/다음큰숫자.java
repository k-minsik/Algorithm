public class 다음큰숫자 {
    class Solution {
        public int solution(int n) {
            int nn = n + 1;
            int compare = Integer.bitCount(n);
            while (true) {
                if (Integer.bitCount(nn) == compare) break;
                nn++;
            }

            return nn;
        }
    }
}
