#include <bits/stdc++.h>
using namespace std;

int n;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;
    queue<int> dq;

    for(int i = 1; i <= n; i++) {
        dq.push(i);
    }

    while(dq.size() != 1) {
        dq.pop();
        dq.push(dq.front());
        dq.pop();
    }

    cout << dq.front() << "\n";

    return 0;
}