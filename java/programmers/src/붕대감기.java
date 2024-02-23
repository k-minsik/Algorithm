import java.util.*;

public class 붕대감기 {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = health;

        int t = bandage[0];
        int x = bandage[1];
        int y = bandage[2];

        int before = 0;
        for (int[] attack : attacks) {
            int time = attack[0];
            int damage = attack[1];

            answer = Math.min(health, answer + (time - before - 1) * x + (time - before - 1) / t * y);
            answer -= damage;

            if (answer <= 0) {
                return -1;
            }

            before = time;
        }

        return answer;
    }
}