import java.util.*;

class Solution {
    public String solution(String input) {
        String answer = "";
        ArrayList<String> store = new ArrayList<>();
        Map<String, Integer> check = new HashMap<>();

        String[] str = input.split("");
        for (int i = 0; i < str.length; i++) {
            if (!check.containsKey(str[i])) {
                check.put(str[i], i);
            } else {
                int before = check.get(str[i]);
                if (i - before == 1) {
                    check.put(str[i], i);
                } else {
                    if (!store.contains(str[i]))
                        store.add(str[i]);
                }
            }
        }

        Collections.sort(store);
        for (String s : store) {
            answer += s;
        }

        return answer.equals("") ? "N" : answer;
    }
}