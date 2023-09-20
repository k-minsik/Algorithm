#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, temp, cnt;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    while(cin >> n) {
        temp = 1;
        cnt = 1;
        while(true) {
            if(temp % n == 0) {
                cout << cnt << "\n";
                break;
            }
            else {
                temp = (temp * 10 + 1) % n;
                cnt++;
            }
        }
    }
    return 0;
}