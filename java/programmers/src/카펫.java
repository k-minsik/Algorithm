public class 카펫 {
    class Solution {
        public int[] solution(int brown, int yellow) {
            int rc = brown + yellow;
            int rcp = (brown + 4) / 2;
            int rcm = (int) Math.sqrt(rcp * rcp - 4 * rc);

            return new int[] {(rcp + rcm) / 2, (rcp - rcm) / 2};
        }
    }
}
