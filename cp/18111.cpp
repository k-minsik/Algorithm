#include <bits/stdc++.h>
using namespace std;

int n, m, b, arr[501][501], ret;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int lowest = 257;
    int highest = -1;
    
    cin >> n >> m >> b;
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> arr[i][j];
            lowest = min(lowest, arr[i][j]);
            highest = max(highest, arr[i][j]);
        }
    }

    int cnt = 1e9;
    for(int h = lowest; h <= highest; h++) {
        int put = 0;
        int take = 0;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                int temp = arr[i][j] - h;
                if (temp > 0) {
                    take += temp;
                }
                else {
                    put -= temp;
                }
            }
        }

        if (put <= take + b) {
            int cnt_temp = 2*take + put;
            if (cnt_temp <= cnt) {
                cnt = cnt_temp;
                ret = h;
            }
        }
    }

    cout << cnt << " " << ret << "\n";

    return 0;
}