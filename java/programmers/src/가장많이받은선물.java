import java.util.*;

public class 가장많이받은선물 {
    class Solution {
        public int solution(String[] fs, String[] gs) {
            Map<String, Integer> convert = new HashMap<>();
            int no = 0;
            for (String f : fs) {
                convert.put(f, no++);
            }

            int[][] graph = new int[no][no];
            int[] point = new int[no];
            for (String g : gs) {
                String[] gg = g.split(" ");

                graph[convert.get(gg[0])][convert.get(gg[1])] += 1;

                point[convert.get(gg[0])] += 1;
                point[convert.get(gg[1])] -= 1;
            }

            int [] answerList = new int[no];
            for (int i = 0; i < no - 1; i++) {
                for (int j = i; j < no; j++) {
                    if (graph[i][j] > graph[j][i]) {
                        answerList[i] += 1;
                    } else if (graph[i][j] < graph[j][i]) {
                        answerList[j] += 1;
                    } else {
                        if (point[i] > point[j]) {
                            answerList[i] += 1;
                        } else if (point[i] < point[j]) {
                            answerList[j] += 1;
                        }
                    }
                }
            }

            int answer = 0;
            for (int a : answerList) {
                answer = Math.max(answer, a);
            }

            return answer;
        }
    }
}
