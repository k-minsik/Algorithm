#include <bits/stdc++.h>
using namespace std;

int n, num, cnt2, cnt5;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cin.tie(NULL);

    cin >> n;

    for(int tk = 0; tk < n; tk++){
        cin >> num;
        cnt2 = 0;
        cnt5 = 0;

        for(int i = 2; i <= num; i*=2) {
            cnt2 += num / i;
        }

        for(int i = 5; i <= num; i*=5) {
            cnt5 += num / i;
        }

        cout << min(cnt2, cnt5) << "\n";
    }
    return 0;
}