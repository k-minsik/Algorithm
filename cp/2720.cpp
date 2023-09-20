#include <bits/stdc++.h>
using namespace std;

int t, Q, D, N, P;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> t;
    Q = 25; D = 10; N = 5; P = 1;

    for(int i = 0; i < t; i++) {
        int money, a, b, c, d;
        cin >> money;

        a = money / Q; money %= Q;
        b = money / D; money %= D;
        c = money / N; money %= N;
        d = money / P; money %= P;

        cout << a << " " << b << " " << c << " " << d << "\n";

    }

    return 0;
}