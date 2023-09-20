#include <bits/stdc++.h>
using namespace std;

int m, a, ret;
string s;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> m;

    for(int i = 0; i < m; i++) {
        cin >> s;
        if (s == "add") {
            cin >> a;
            ret |= (1 << a);
        }
        else if (s == "remove") {
            cin >> a;
            ret &= ~(1 << a);
        }
        else if (s == "check") {
            cin >> a;
            if (ret & (1 << a)) {
                cout << 1 << "\n";
            }
            else {
                cout << 0 << "\n";
            }
        }
        else if (s == "toggle") {
            cin >> a;
            ret ^= (1 << a);
        }
        else if (s == "all") {
            ret = (1 << 21) - 1;
        }
        else if (s == "empty") {
            ret = 0;
        }
    }

    return 0;
}