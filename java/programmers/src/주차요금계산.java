import java.util.*;

public class 주차요금계산 {
    class Solution {
        public int[] solution(int[] fees, String[] records) {
            Map<String, Integer> totalParkingTime = new HashMap<>();
            Map<String, Integer> inTimeMap = new HashMap<>();

            for (String record : records) {
                String[] splitRecord = record.split(" ");
                String[] timeSplit = splitRecord[0].split(":");
                int time = Integer.parseInt(timeSplit[0]) * 60 + Integer.parseInt(timeSplit[1]);
                String carNumber = splitRecord[1];
                String status = splitRecord[2];

                if (status.equals("IN")) {
                    inTimeMap.put(carNumber, time);
                } else {
                    int parkedTime = time - inTimeMap.remove(carNumber);
                    totalParkingTime.put(carNumber, totalParkingTime.getOrDefault(carNumber, 0) + parkedTime);
                }
            }

            // 처리되지 않은 입차 기록 처리
            for (Map.Entry<String, Integer> entry : inTimeMap.entrySet()) {
                int parkedTime = 1439 - entry.getValue();
                totalParkingTime.put(entry.getKey(), totalParkingTime.getOrDefault(entry.getKey(), 0) + parkedTime);
            }

            // 차량 번호 순으로 정렬
            List<String> carNumbers = new ArrayList<>(totalParkingTime.keySet());
            Collections.sort(carNumbers);

            ArrayList<Integer> answer = new ArrayList<>();
            for (String carNumber : carNumbers) {
                int time = totalParkingTime.get(carNumber);
                int fee = fees[1];
                if (time > fees[0]) {
                    fee += Math.ceil((double)(time - fees[0]) / fees[2]) * fees[3];
                }
                answer.add(fee);
            }

            return answer.stream().mapToInt(i -> i).toArray();
        }
    }

}
