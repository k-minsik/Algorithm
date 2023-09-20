#include <bits/stdc++.h>
using namespace std;

int x, answer = 1;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> x;

    while(x != 1) {
        if (x & 1){
            answer++;
        }
        x /= 2;
    }

    cout << answer << "\n";
    return 0;
}

